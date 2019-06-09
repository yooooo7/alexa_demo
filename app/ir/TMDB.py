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

# get similar movie based on a specific moive
def movie_similars(movie_id, page: int = 1) -> object:
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    page -- page number of similar movies
    
    Returns:
    json formatted similar movies list
    """
    url = f'{HOST}movie/{movie_id}/similar'
    p = { 'page': page, 'language': 'en-US' }
    query = {**params, **p}
    return send_request(url, query)

 # search movie by movie title
def get_movie(movie_title: str, page: int = 1, year: int = None, primary_release_year: int = None) -> object:
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

# get movie detail by movie id
def get_movie_detail(movie_id) -> object:
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    
    Returns:
    json formatted movie details
    """
    url = '{}movie/{}'.format(HOST, movie_id)
    query = {**params}
    return send_request(url, query)

# search movie date
def get_movie_release_date(movie_id) -> object:
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    
    Returns:
    json formatted movies released date
    """
    url = '{}movie/{}/release_dates'.format(HOST, movie_id)
    query = {**params}
    return send_request(url, query)

# search movie by actor name
def get_person(actor_name: str, page: int = 1) -> object:
    """
    Arguments:
    movie_title -- name of a movie
    page -- page number of result
    include_adult -- adult movie
    region -- country
    
    Returns:
    json formatted response of movie list
    """
    url = '{}search/person'.format(HOST)
    p = {
        'language': 'en-US',
        'query': actor_name,
        'page': page,
        'include_adult': 'false',
        'region': None
    }
    query = {**params, **p}
    return send_request(url, query)

def get_person_detail(person_id):
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    
    Returns:
    json formatted movie details
    """
    url = '{}person/{}'.format(HOST, person_id)
    query = {**params}
    return send_request(url, query)

# get movie reviews
def get_movie_reviews(movie_id, page: int = 1) -> object:
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
def get_movie_credits(movie_id) -> object:
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    
    Returns:
    json formatted movie related people (actors and staffs) list
    """
    url = '{}movie/{}/credits'.format(HOST, movie_id)
    p = {}
    query = {**params, **p}
    return send_request(url, query)
