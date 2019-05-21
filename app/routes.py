from flask import request, Response

from app import app

from .preprocessing import normalization
from .preprocessing import mapping

from .ir import search_movie, search_movie_overview_reviews
from .nlg import movie_reviews_summarise_sentiment, sentimentIntensity_analyzer, lexRank_summarizer

import json

@app.route('/test', methods = ['POST'])
def test():
    # check if request body exist
    if not request.json:
        return Response(json.dumps({'error': 'Input should be in json format'}), mimetype='application/json')
    if 'input' not in request.json:
        return Response(json.dumps({'error': 'Input is needed'}), mimetype='application/json')
    
    # get user input
    sentence = request.json['input']
    # normalization
    normal_sentence = normalization(sentence)
    # mapping key word
    _, movie_title = mapping(normal_sentence)

    if not movie_title:
        return Response(json.dumps({'output': 'I don\'t know this movie right now'}), mimetype='application/json')

    movie_title = ' '.join(movie_title)

    # get movie reviews list
    try:
        search_result = search_movie_overview_reviews(movie_title)
    except Exception as e:
        return Response(json.dumps({'error': 'TMDB API error {}'.format(e.args)}), mimetype='application/json')
    
    if search_result == None:
        return Response(json.dumps({'error': 'TMDB API didn\'t find any result'}), mimetype='application/json')
    
    reviews = search_result['reviews']

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