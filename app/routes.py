from flask import request, Response

from app import app

from .ir import search_movie, search_movie_overview_reviews, search_movie_actors, search_movie_title
from .nlu import NLU
from .nlg import movie_reviews_summarise_sentiment, sentimentIntensity_analyzer, lexRank_summarizer
from .nlg import ROOT, dialog_mapping

import json
from collections import Counter
import random

current_node = None
last_entities = (None, None)

@app.route('/', methods = ['GET'])
def index():
    return Response(json.dumps({'hello': 'your server is running successfully!'}), mimetype='application/json')

@app.route('/dialog', methods = ['POST'])
def dialogue_flow():
    global current_node
    global last_entities

    # check request
    has_request, message = check_request()
    if not has_request:
        clear_globals()
        return Response(json.dumps(message), mimetype='application/json')
    
    # NLU
    entities, user_sentiment = NLU(message)
    print(entities, last_entities)
    if entities == (None, None):
        entities = last_entities
    else:
        last_entities = entities

    # renew current node
    isExist, current_node = dialog_manager(current_node, user_sentiment, entities[1])
    if not isExist:
        message = current_node
        clear_globals()
        return Response(json.dumps({ 'error': message }), mimetype='application/json')

    current_node.sentiment = user_sentiment
    current_node.entities = entities

    sentence = current_node.template2sentence(entities[1])
    
    return Response(json.dumps({ 'output': sentence }), mimetype='application/json')

def check_match(item, items):
    if items is None or items is 'any':
        return True

    if item in items:
        return True

    return False

def dialog_manager(cuurent_node, sentiment, entities):
    if current_node is None:
        return True, ROOT

    if current_node not in dialog_mapping:
        return False, 'node not in mapping'

    node_candidates = dialog_mapping[current_node]
    for node in node_candidates:
        current_sentiments = node_candidates[node]['sentiment']
        current_entities = node_candidates[node]['entities']
        if check_match(sentiment, current_sentiments) and check_match(entities, current_entities):
            return True, node
    
    return False, 'did not find any nodes'

def clear_globals():
    global current_node
    global last_entities
    current_node = None
    last_entities = (None, None)

def check_request():
    # check if request body exist
    if not request.json:
        return False, {'error': 'Input should be in json format'}
    if 'input' not in request.json:
        return False, {'error': 'Input is needed'}

    return True, request.json['input']
