from flask import request, Response

from app import app

from .ir import search_movie, search_movie_overview_reviews, search_movie_actors, search_movie_title
from .nlu import NLU, topic_detection
from .nlg import movie_reviews_summarise_sentiment, sentimentIntensity_analyzer, lexRank_summarizer
from .nlg import MOVIE_TEMPLATE, GREETING_TAMPLATE

import json
from collections import Counter
import random

greeting_dialog_counter = 0
dialog_counter = {
    'movie': 0,
    'sport': 0
}
current_topic = None
movie_title = None

@app.route('/', methods = ['GET'])
def index():
    return Response(json.dumps({'hello': 'your server is running successfully!'}), mimetype='application/json')

@app.route('/dialog', methods = ['POST'])
def dialogue_flow():
    global greeting_dialog_counter
    global dialog_counter
    global current_topic
    global movie_title

    # check request
    has_request, message = check_request()
    if not has_request:
        clear_globals()
        return Response(json.dumps(message), mimetype='application/json')
    
    entity, user_sentiment = NLU(message)

    if greeting_dialog_counter < len(GREETING_TAMPLATE):

        candidates = GREETING_TAMPLATE[greeting_dialog_counter]
        greeting_dialog_counter += 1

        sentimentTemplate = sentiment_temp(candidates, user_sentiment)
        template = sentimentTemplate + random.sample(candidates['templates'], 1)[0]
    else:
        # topic id
        if list(dialog_counter.values()) == [0] * len(dialog_counter):
            current_topic = topic_detection(message)
            if current_topic is None:
                Response(json.dumps({ 'output': 'I am still learning this topic' }), mimetype='application/json')
                return
        
        current_template = MOVIE_TEMPLATE if current_topic == 'movie' else None # Todo
        current_counter = dialog_counter[current_topic]
        candidates = current_template[current_counter]
        
        dialog_counter[current_topic] += 1

        sentimentTemplate = sentiment_temp(candidates, user_sentiment)
        isVaild, entityTemplate = entity_temp(candidates, entity, user_sentiment)
        if not isVaild:
            clear_globals()
            return Response(json.dumps({ 'error': entityTemplate }), mimetype='application/json')
        template = sentimentTemplate + entityTemplate + random.sample(candidates['templates'], 1)[0]
    return Response(json.dumps({ 'output': template }), mimetype='application/json')

def clear_globals():
    global greeting_dialog_counter
    global dialog_counter
    global current_topic
    global movie_title

    greeting_dialog_counter = 0
    current_topic = None
    dialog_counter = {'movie': 0, 'sport': 0}
    movie_title = None

def entity_temp(candidates, entity, user_sentiment):
    global movie_title

    entityTypes = candidates['entityType']
    if entityTypes is None:
            return True, ''

    entityTemplate = ''
    for entityType in entityTypes:

        if entityType == 'MovieActor':
            # find two actors of the movie
            if entity[1] is not None:
                movie_title = ' '.join(entity[1])
            
            if movie_title is None:
                return False, 'Did not detect any movie title'

            try:
                actors = search_movie_actors(movie_title)
            except Exception as e:
                return False, 'TMDB API error {}'.format(e.args)
            
            if len(actors) < 2:
                return False, 'Don\'t have enough actors information'
            
            entityTemplate += random.sample(candidates['MovieActorTemplates'], 1)[0].format(actors[0], actors[1])
        
        if entityType == 'MovieName':
            if entity[1] is not None:
                movie_title = ' '.join(entity[1])
            
            if movie_title is None:
                return False, 'Did not detect any movie title'
            
            try:
                movie_name = search_movie_title(movie_title)
            except Exception as e:
                return False, 'TMDB API error {}'.format(e.args)

            entityTemplate += random.sample(candidates['MovieNameTemplates'], 1)[0].format(movie_name)
        
        if entityType == 'MovieDes':
            if entity[1] is not None:
                movie_title = ' '.join(entity[1])
            
            if movie_title is None:
                return False, 'Did not detect any movie title'
            
            try:
                movie_des = search_movie_overview_reviews(movie_title)['overview']
            except Exception as e:
                return False, 'TMDB API error {}'.format(e.args)

            entityTemplate += random.sample(candidates['MovieDesTemplates'], 1)[0].format(movie_des)

        # if entityType == 'Reviews':
        #     try: 
        #         isValid, reviews = sentence2reviews(entity[1], user_sentiment)
        #     except Exception as e:
        #         return False, 'TMDB API error {}'.format(e.args)

        #     entityTemplate += random.sample(candidates['ReviewsTemplates'], 1)[0].format(reviews)
        
        # if entityType == 'MovieActor1':
        #     movie_title = ' '.join(entity[1])
        #     try:
        #         actors = search_movie_actors(movie_title)
        #     except Exception as e:
        #         return False, 'TMDB API error {}'.format(e.args)   
        #     if len(actors) < 2:
        #             return False, 'Don\'t have enough actors information'
                
        #     entityTemplate += random.sample(candidates['MovieActor1Templates'], 1)[0].format(actors[0], actors[1])
        
        # if entityType == 'MovieLable':
        #     movie_title = ' '.join(entity[1])
        #     pass
        
        # if entityType == 'ActorMovie':
        #     entityTemplate += random.sample(candidates['ActorMovieTemplates'], 1)[0].format(actors[0])

        # if entityType == 'RecommonActor2Movie':
        #     pass       
    return (False, 'do not find vaild entity type') if entityTemplate is '' else (True, entityTemplate)

def sentiment_temp(candidates, user_sentiment):
    if not candidates['needSentiment']:
        return ''

    if user_sentiment not in ['pos', 'neg']:
        user_sentiment = 'other'
    sentimentTemplate = random.sample(candidates['sentimentTemplates'][user_sentiment], 1)[0]
    
    return sentimentTemplate

def check_request():
    # check if request body exist
    if not request.json:
        return False, {'error': 'Input should be in json format'}
    if 'input' not in request.json:
        return False, {'error': 'Input is needed'}

    return True, request.json['input']

def sentence2reviews(movie_title, user_sentiment):
    # get movie reviews list
    try:
        search_result = search_movie_overview_reviews(movie_title)
        for i in range(len(search_result)):
            if search_result[i]['sentiment'] == user_sentiment:
                reviews = search_result[i]['summary']
                #reviews = search_result[i]['reviews']
            break
        
    except Exception as e:
        return False, {'error': 'TMDB API error {}'.format(e.args)}
    
    if search_result == None:
        return False, {'error': 'TMDB API didn\'t find any result'}
    
    
    return True, reviews