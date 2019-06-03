import requests

# set constant variables
API_KEY = '5e1252eceeb2b4e0f784b73538d47d65'
HOST = 'https://api.themoviedb.org/3/'

params = {
    'api_key': API_KEY
}

# send request and get json response
def send_request(url: str, params: object) -> object:
    r = requests.get(url, params = params)
    try:
        response = r.json()
    except Exception as e:
        response = 'parse json error: {}'.format(e.args)
    return response

# search movie by movie title
def search_movie(movie_title: str, page: int = 1, year: int = None, primary_release_year: int = None) -> object:
    """
    Arguments:
    movie_title -- name of a movie
    page -- page number of result
    year -- year of the movie
    primary_release_year -- primary release year of movie
    
    Returns:
    json formatted response of movie list
    """
    url = '{}search/movie'.format(HOST)
    p = {
        'language': 'en-US',
        'query': movie_title,
        'page': page,
        'year': year,
        'primary_release_year': primary_release_year
    }
    query = {**params, **p}
    return send_request(url, query)

def search_movie_title(movie_title: str, page: int = 1, year: int = None, primary_release_year: int = None) -> object:
    # get search results by search movie API
    search_results = search_movie(movie_title, year = year, primary_release_year = primary_release_year)

    # if error occur print that error and return None
    if 'results' not in search_results:
        print(search_results)
        return None

    search_results = search_results['results']

    # check if result exist
    if len(search_results) == 0:
        print('Can not find any results')
        return None

    # get current movie overview and ID
    searched_movie = search_results[0]
    movie_name = searched_movie['title']
    
    return movie_name

# get movie reviews
def movie_reviews(movie_id, page: int = 1) -> object:
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    page -- page number of reviews
    
    Returns:
    json formatted movie reviews list
    """
    url = '{}movie/{}/reviews'.format(HOST, movie_id)
    p = { 'page': page }
    query = {**params, **p}
    return send_request(url, query)

# get movie related actors and staffs information
def movie_credits(movie_id) -> object:
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    
    Returns:
    json formatted movie related people (actors and staffs) list
    """
    url = f'{HOST}movie/{movie_id}/credits'
    p = {}
    query = {**params, **p}
    return send_request(url, query)

def search_movie_actors(movie_title: str, year: int = None, primary_release_year:int = None, k: int = 0) -> list:
    # get search results by search movie API
    search_results = search_movie(movie_title, year = year, primary_release_year = primary_release_year)

    # if error occur print that error and return None
    if 'results' not in search_results:
        print(search_results)
        return None

    search_results = search_results['results']

    # check if result exist
    if len(search_results) == 0:
        print('Can not find any results')
        return None

    # get current movie overview and ID
    searched_movie = search_results[0]
    movie_id = searched_movie['id']

    # get movie actors by movie credits API
    actor_results = movie_credits(movie_id)['cast']
    actors = [ actor['name'] for actor in actor_results ]

    return actors[:k] if k <= len(actors) else actors

def search_movie_overview(movie_title: str, year: int = None, primary_release_year:int = None):
    return search_movie_overview_reviews(movie_title, year, primary_release_year)['overview']

# get movie overview and reviews based on movie title
def search_movie_overview_reviews(movie_title: str, year: int = None, primary_release_year:int = None) -> object:
    """
    Arguments:
    movie_title -- name of a movie
    year -- year of the movie
    primary_release_year -- primary release year of movie

    Returns:
    a object has two fields:
    overview -- the overview of first resopnsed movie
    reviews -- a list of reviews of first responsed movie
    """
    # get search results by search movie API
    search_results = search_movie(movie_title, year = year, primary_release_year = primary_release_year)

    # if error occur print that error and return None
    if 'results' not in search_results:
        print(search_results)
        return None

    search_results = search_results['results']

    # check if result exist
    if len(search_results) == 0:
        print('Can not find any results')
        return None

    # get current movie overview and ID
    searched_movie = search_results[0]
    movie_overview, movie_id = searched_movie['overview'], searched_movie['id']

    # get movie reviews by movie reviews API
    review_results = movie_reviews(movie_id)['results']
    reviews = [ review['content'] for review in review_results ]

    return { 'overview': movie_overview, 'reviews': reviews }