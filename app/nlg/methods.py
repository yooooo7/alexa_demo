from ..ir import get_movie, get_movie_detail, get_movie_credits, get_movie_release_date, get_movie_reviews, get_person, get_person_detail, movie_similars
from .summarizers import lexRank_summarizer
from ..nlu import dic

def check_response(search_results):
     # if error occur print that error and return None
    if 'results' not in search_results:
        return False, 'API query error: ' + search_results

    # check if result exist
    if len(search_results) == 0:
        return False, 'API query Can not find any results'
    
    return True, None


def search_2_sug_movies(movie_title):
    # get search results by search movie API
    search_results = get_movie(movie_title)

    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message

    # get current movie overview and ID
    searched_movie = search_results['results'][0]
    movie_id = searched_movie['id']

    # get similar movies
    movies = movie_similars(movie_id)
    
    # response validation
    isValid, error_message = check_response(movies)
    if not isValid:
        return False, error_message
    
    movie_results = movies['results']
    movies = [ movie['title'] for movie in movie_results ]
    print(movie_results, movies)

    if len(movies) < 2:
        return False, 'do not have enough similar movies'
    
    movies = movies[:2]
    
    # add actors to dic
    for movie in movies:
        dic.append([movie, 'MOVIE_TITLE'])

    return True, movies

def search_2_movie_actors(movie_title: str) -> list:
    # get search results by search movie API
    search_results = get_movie(movie_title)

    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message

    # get current movie overview and ID
    searched_movie = search_results['results'][0]
    movie_id = searched_movie['id']

    # get movie actors by movie credits API
    actor_results = get_movie_credits(movie_id)['cast']
    actors = [ actor['name'] for actor in actor_results ]

    if len(actors) < 2:
        return False, 'do not have enough actors'
    
    actors = actors[:2]
    
    # add actors to dic
    for actor in actors:
        dic.append([actor, 'ACTORS'])

    return True, actors

# get movie label based on movie name
def search_movie_labels(movie_title: str): 
    # get search results by search movie API
    search_results = get_movie(movie_title)
    
    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message

    # get movie id
    search_result = search_results['results'][0]
    movie_id = search_result['id']

    #get genres 
    genres = get_movie_detail(movie_id)['genres']
    return True, [ ' '.join([genre['name'] for genre in genres]) ]

def search_movie_release_date(movie_title: str):
    # get search results by search movie API
    search_results = get_movie(movie_title)

    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message
    
    # get movie id
    search_result = search_results['results'][0]
    movie_id = search_result['id']

    #get release date
    search_results = get_movie_release_date(movie_id)

    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message
    
    dates = search_results['results'][0]['release_dates']
    date = dates[0]['release_date']
    
    return True, [ date.split('-')[0] ]

def movie_overview_summary(movie_title):
    # get search results by search movie API
    search_results = get_movie(movie_title)

    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message

    # get current movie overview
    searched_movie = search_results['results'][0]
    movie_overview = searched_movie['overview']

    return True, [ lexRank_summarizer(movie_overview, 2) ]

def movie_review_summary(movie_title):
    # get search results by search movie API
    search_results = get_movie(movie_title)

    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message

    # get current movie ID
    searched_movie = search_results['results'][0]
    movie_id = searched_movie['id']

    # get movie reviews by movie reviews API
    review_results = get_movie_reviews(movie_id)
    
    # response validation
    isValid, error_message = check_response(review_results)
    if not isValid:
        return False, error_message
    
    # get movie id
    review = review_results['results'][0]
    review_content = review['content']

    return True, [ lexRank_summarizer(review_content, 2) ]

def search_actor_gender(person_name):
    # get search results by search movie API
    search_results = get_person(person_name)

    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message
    
    # get person id
    person = search_results['results'][0]
    person_id = person['id']

    # get bio gender
    detail = get_person_detail(person_id)
    gender = 'He' if detail['gender'] == 2 else 'She'

    return True, [gender]

def search_actor_birth_gender(person_name):
    # get search results by search movie API
    search_results = get_person(person_name)

    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message
    
    # get person id
    person = search_results['results'][0]
    person_id = person['id']

    detail = get_person_detail(person_id)
    birthday = detail['birthday']
    birthPlace = detail['place_of_birth']
    gender = 'He' if detail['gender'] == 2 else 'She'

    return True, [ gender, birthday, birthPlace, gender ]

def search_actor_bio_gender(person_name):
    # get search results by search movie API
    search_results = get_person(person_name)

    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message
    
    # get person id
    person = search_results['results'][0]
    person_id = person['id']

    # get bio gender
    detail = get_person_detail(person_id)
    bio, gender = detail['biography'], 'He' if detail['gender'] == 2 else 'She'

    return True, [ lexRank_summarizer(bio, 2), gender ]

def search_actor_2_movies(person_name):
    # get search results by search movie API
    search_results = get_person(person_name)

    # response validation
    isValid, error_message = check_response(search_results)
    if not isValid:
        return False, error_message
    
    # get person id
    person = search_results['results'][0]
    movies = person['known_for']
    
    if len(movies) < 2:
        return False, 'do not have enough related movies'
    
    movies = movies[:2]

    movie_titles = [movie['title'] for movie in movies]
    
    # add movies to dic
    for movie_title in movie_titles:
        dic.append([movie_title, 'MOVIE_TITLE'])

    return True, movie_titles