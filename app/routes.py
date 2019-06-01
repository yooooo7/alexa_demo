from flask import request, Response

from app import app

from .ir import search_movie, search_movie_overview_reviews
from .nlu import NLU
from .nlg import movie_reviews_summarise_sentiment, sentimentIntensity_analyzer, lexRank_summarizer

import json
from collections import Counter
import random

dialog_counter = 0

TAMPLATE = [
    { 
        'needSentiment': False,
        'entityType': None,
        'templates':  ['Hi, this is Sydney Jack. How are you?', 'how are you?', 'how\'s it going?']
    },
    { 
        'needSentiment': True,
        'entityType': None,
        'sentimentTemplates':  {
            'pos': ['That\'s good!', 'Great!'],
            'other': [''],
            'neg': ['Sorry to hear that.']
        },
        'templates': ['Sports or movies are topics you could be interested in and we could talk about any of them.']
    },
    { 
        'needSentiment': False,
        'entityType': ['Movie', 'Sport'],
        'MovieTemplates': [
            'Sure. Have you seen a movie recently?', 
            'No problem. Did you see a movie these days?', 
            'Certainly. Have you watched a film over the past few days?'
        ],
        'SportTemplates': [''],
        'templates': ['']
    },
    { 
        'needSentiment': False,
        'entityType': ['MovieActor'],
        'MovieActorTemplates': [
            'Is that the film with {} and {}?', 
            'Is that movie the one depicting {} and {}?', 
            'Are {} and {} the stars in the movie?'
        ],
        'templates': ['']
    }
]

@app.route('/', methods = ['GET'])
def index():
    return Response(json.dumps({'hello': 'your server is running successfully!'}), mimetype='application/json')

def semtiment_rate(result):
    # count sentiments
    sentiments = [ item['sentiment'] for item in result ]
    sentiments_count = Counter(sentiments)
    
    # calculate rates
    sentiment_rates = {}
    total = len(sentiments)
    for sentiment in sentiments_count:
        rate = sentiments_count[sentiment] / total
        sentiment_rates[sentiment] = round(rate, 2)
    
    return Response(json.dumps({ 'output': sentiment_rates }), mimetype='application/json')

@app.route('/dialog', methods = ['POST'])
def dialogue_flow():
    global dialog_counter

    # check request
    has_request, message = check_request()
    if not has_request:
        return Response(json.dumps(message), mimetype='application/json')
    
    entity, user_sentiment = NLU(message)

    candidates = TAMPLATE[dialog_counter]
    sentimentTemplate = ''
    if candidates['needSentiment']:
        if user_sentiment not in ['pos', 'neg']:
            user_sentiment = 'other'
        sentimentTemplate = random.sample(candidates['sentimentTemplates'][user_sentiment], 1)[0]
    
    template = sentimentTemplate + ' ' + random.sample(candidates['templates'], 1)[0]

    dialog_counter = 0 if (dialog_counter + 1) >= len(TAMPLATE) else dialog_counter + 1

    return Response(json.dumps({ 'output': template }), mimetype='application/json')

def dialog_logic(dialog_counter):
    pass

def check_request():
    # check if request body exist
    if not request.json:
        return False, {'error': 'Input should be in json format'}
    if 'input' not in request.json:
        return False, {'error': 'Input is needed'}

    return True, request.json['input']

def sentence2reviews(movie_title):
    if not movie_title:
        return False, {'output': 'I don\'t know this movie right now'}

    movie_title = ' '.join(movie_title)

    # get movie reviews list
    try:
        search_result = search_movie_overview_reviews(movie_title)
    except Exception as e:
        return False, {'error': 'TMDB API error {}'.format(e.args)}
    
    if search_result == None:
        return False, {'error': 'TMDB API didn\'t find any result'}
    
    reviews = search_result['reviews']

    return True, [movie_title, reviews]