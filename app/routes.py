from flask import request, Response

from app import app

from .nlu import NLU
from .nlg import movie_reviews_summarise_sentiment, sentimentIntensity_analyzer, lexRank_summarizer
from .nlg import ROOT, dialog_mapping

import json
from collections import Counter
import random

current_node = None
last_entity = None

@app.route('/', methods = ['GET'])
def index():
    return Response(json.dumps({'hello': 'your server is running successfully!'}), mimetype='application/json')

@app.route('/dialog', methods = ['POST'])
def dialogue_flow():
    global current_node
    global last_entity

    # check request
    has_request, message = check_request()
    if not has_request:
        clear_globals()
        return Response(json.dumps(message), mimetype='application/json')
    
    # NLU
    user_sentiment, entity, user_intent = NLU(message).values()

    # Quit
    if user_intent == 'quit':
        clear_globals()
        return Response(json.dumps({ 'output': 'Nice to see you agian' }), mimetype='application/json')

    # check if need to renew entity
    _, entity_content = entity
    if entity_content == None:
        entity_content = last_entity
    else:
        last_entity = entity_content

    # renew current node
    isExist, current_node = dialog_manager(current_node, user_sentiment, user_intent)
    if not isExist:
        message = current_node
        clear_globals()
        return Response(json.dumps({ 'error': message }), mimetype='application/json')

    sentence = current_node.template2sentence(entity_content)
    
    return Response(json.dumps({ 'output': sentence }), mimetype='application/json')

def check__sentiment(item, items):
    if items is None:
        return True
    
    if items is 'any' and item is not None:
        return True

    if item in items:
        return True

    return False

def check_intent(item, intent):
    if intent is None:
        return True
    
    if intent is 'any' and item is not None:
        return True
    
    if item == intent:
        return True
    
    return False

def dialog_manager(current_node, sentiment, intent):
    if current_node is None:
        return True, ROOT

    if current_node not in dialog_mapping:
        return False, 'node not in mapping'

    node_candidates = dialog_mapping[current_node]
    for node in node_candidates:
        current_sentiments = node_candidates[node]['sentiment']
        current_intent = node_candidates[node]['intent']
        if check__sentiment(sentiment, current_sentiments) and check_intent(intent, current_intent):
            return True, node
    
    return False, 'did not find any nodes'

def clear_globals():
    global current_node
    global last_entity
    current_node = None
    last_entity = None

def check_request():
    # check if request body exist
    if not request.json:
        return False, {'error': 'Input should be in json format'}
    if 'input' not in request.json:
        return False, {'error': 'Input is needed'}

    return True, request.json['input']
