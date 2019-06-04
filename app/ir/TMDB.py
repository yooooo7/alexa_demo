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

# get movie detail by movie id
def get_movie_detail(movie_id) -> object:
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    
    Returns:
    json formatted movie details
    """
    url = f'{HOST}movie/{movie_id}'
    query = {**params}
    return send_request(url, query)

# search movie date
def get_movie_date(movie_id) -> object:
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    
    Returns:
    json formatted movies released date
    """
    url = f'{HOST}movie/{movie_id}/release_dates'
    query = {**params}
    return send_request(url, query)

# search movie by actor name
def search_movie_byActor( region: str, actor_name: str, page: int = 1) -> object:
    """
    Arguments:
    movie_title -- name of a movie
    page -- page number of result
    include_adult -- adult movie
    region -- country
    
    Returns:
    json formatted response of movie list
    """
    url = f'{HOST}search/person'
    p = {
        'language': 'en-US',
        'query': actor_name,
        'page': page,
        'include_adult': 'false',
        'region': None
    }
    query = {**params, **p}
    return send_request(url, query)

# get movie reviews
def movie_reviews(movie_id, page: int = 1) -> object:
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    page -- page number of reviews
    
    Returns:
    json formatted movie reviews list
    """
    url = f'{HOST}movie/{movie_id}/reviews'
    p = { 'page': page }
    query = {**params, **p}
    return send_request(url, query)

# get movie overview
def movie_overview(movie_id, page: int = 1) -> object:
    """
    Arguments:
    movie_id -- TMDB/IMDB movie ID
    page -- page number of reviews
    
    Returns:
    json formatted movie reviews list
    """
    url = f'{HOST}movie/{movie_id}/reviews'
    p = { 'page': page }
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
    
    return [movie_name]

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

def search_movie_2_actors(movie_title: str, year: int = None, primary_release_year:int = None):
    actors = search_movie_actors(movie_title, year = year, primary_release_year = primary_release_year, k = 2)
    if len(actors) < 2:
        return ['do not have enough actors', 'do not have enough actors']
    return actors

def search_movie_overview(movie_title: str, year: int = None, primary_release_year:int = None):
    res = search_movie_overview_reviews(movie_title, year, primary_release_year)
    return [ res['overview'] if res is not None else res ]

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


# get movie label based on movie name
def search_movie_labels(movie_name:str) ->object:
    """
    Arguments:
    movie_name -- name of a movie
    """
    
    # get search results by search movie API
    search_results = search_movie(movie_name)
    
    # if error occur print that error and return None
    if 'results' not in search_results:
        print(search_results)
        return None

    # check if result exist
    if len(search_results) == 0:
        print('Can not find any results')
        return None
    
    # get movie id
    movie_Id = search_results['results'][0]['id']
    #get genres 
    genres = get_movie_detail(movie_Id)['genres']
    l = []
    for i in range(len(genres)):
            l.append(genres[i]['name'])
    return l


def search_movie_reviews(movie_name:str) ->object:
    # get search results by search movie API
    search_results = search_movie(movie_name)
    
    # if error occur print that error and return None
    if 'results' not in search_results:
        print(search_results)
        return None

    # check if result exist
    if len(search_results) == 0:
        print('Can not find any results')
        return None
    
    # get movie id
    movie_Id = search_results['results'][0]['id']
    
    # get movie review
    if movie_reviews(movie_Id)!= None:
        review_results = movie_reviews(movie_Id)['results']
        if review_results:
            if review_results[0]:
                if 'content' in review_results[0]== True:
                    review = str(review_results[0]['content'])
                    return review
                else: 
                    review = ['I agree with you']
                    return review
            else: 
                review = ['i totally agree with you']
                return review
        else: 
            review = ['i totally agree with you']
            return review
    else: 
        review = ['yeah']
        return review





def search_movie_date(actor_name:str) ->object:
    movies_results = search_movie_byActor('',actor_name)
    # if error occur print that error and return None
    if 'results' not in movies_results:
        print(movies_results)
        return None

    # check if result exist
    if len(movies_results) == 0:
        print('Can not find any results')
        return None
    
    # get movie id

    movie_Id = movies_results['results'][0]['id']


    #get release date
    date = get_movie_date(movie_Id)['results'][0]['release_dates'][0]['release_date']
    year = [date][0][:4]
    year = [year][0]

    return [year]









def search_actor_movie(actor_name:str) ->object:
    # get movie results by search actor name 
    movies_results = search_movie_byActor('',actor_name)
    
     # if error occur print that error and return None
    if 'results' not in movies_results:
        print(movies_results)
        return None

    # check if result exist
    if len(movies_results) == 0:
        print('Can not find any results')
        return None
    
    # get movie title 
    if movies_results['results']:
        if movies_results['results'][0]:
            if movies_results['results'][0]['known_for']:
                if movies_results['results'][0]['known_for'][0]:
                    if movies_results['results'][0]['known_for'][0]['title']:
                        movie = movies_results['results'][0]['known_for'][0]['title']
                        return [movie]
                    else: 
                        movie = ['I have not watched others'] 
                        return movie
                else:
                    movie = ['I have not watched others'] 
                    return movie
            else:
                movie = ['I have not watched others'] 
                return movie
        else:
            movie = ['I have not watched others'] 
            return movie
    else: 
       movie = ['I have not watched others'] 
       return movie

    movie = movies_results['results'][0]['known_for'][0]['title']

    return movie


def search_actor_description(actor_name:str) ->object:
    # get movie results by search actor name 
    movies_results = search_movie_byActor('',actor_name)
    
     # if error occur print that error and return None
    if 'results' not in movies_results:
        print(movies_results)
        return None

    # check if result exist
    if len(movies_results) == 0:
        print('Can not find any results')
        return None
    
    
    # get movie description 
    description = movies_results['results'][0]['known_for'][0]['overview']
    return [description]

