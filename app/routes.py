from flask import request, Response

from app import app

from .preprocessing import normalization
from .preprocessing import mapping

from .ir import search_movie, search_movie_overview_reviews
from .nlg import movie_reviews_summarise_sentiment, sentimentIntensity_analyzer, lexRank_summarizer

import json
from collections import Counter

@app.route('/', methods = ['GET'])
def index():
    return Response(json.dumps({'hello': 'your server is running successfully!'}), mimetype='application/json')

@app.route('/test', methods = ['POST'])
def test():
    # check request
    has_request, message = check_request()
    if not has_request:
        return Response(json.dumps(message), mimetype='application/json')
    
    # sentence to movie reviews
    has_reviews, message = sentence2reviews()
    if not has_reviews:
        return Response(json.dumps(message), mimetype='application/json')
    movie_title, reviews = message

    # do summarisation and sentiment analysis
    result = movie_reviews_summarise_sentiment(
        movie_title = movie_title,
        reviews = reviews,
        summarizer = lexRank_summarizer,
        summary_max_length = 2,
        analyzer = sentimentIntensity_analyzer
    )

    output = result[0]['summary']

    return Response(json.dumps({'output': output}), mimetype='application/json')

@app.route('/sentiment/rate', methods = ['POST'])
def semtiment_rate():
    # check request
    has_request, message = check_request()
    if not has_request:
        return Response(json.dumps(message), mimetype='application/json')
    
    # sentence to movie reviews
    has_reviews, message = sentence2reviews()
    if not has_reviews:
        return Response(json.dumps(message), mimetype='application/json')
    movie_title, reviews = message

    # do summarisation and sentiment analysis
    result = movie_reviews_summarise_sentiment(
        movie_title = movie_title,
        reviews = reviews,
        summarizer = lexRank_summarizer,
        summary_max_length = 2,
        analyzer = sentimentIntensity_analyzer
    )
    
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

def check_request():
    # check if request body exist
    if not request.json:
        return False, {'error': 'Input should be in json format'}
    if 'input' not in request.json:
        return False, {'error': 'Input is needed'}

    return True, None

def sentence2reviews():
    # get user input
    sentence = request.json['input']
    # normalization
    normal_sentence = normalization(sentence)
    # mapping key word
    _, movie_title = mapping(normal_sentence)

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