movie_dict = [
    [['star', 'war'], 'MOVIE_TITLE'], 
    [['avenger'], 'MOVIE_TITLE'], 
    [['the', 'avenger'], 'MOVIE_TITLE'],
    [['beauty', 'and', 'the', 'beast'], 'MOVIE_TITLE'], 
    [['iron', 'man'], 'MOVIE_TITLE'], 
    [['captain', 'america'], 'MOVIE_TITLE']
]
topics = ['movie', 'sport']

def mapping (user_input: list):
    for i in range(len(movie_dict)):
        common_part= [j for j in user_input if j in movie_dict[i][0]]
        if len(common_part) == len(movie_dict[i][0]):
            return movie_dict[i][1], common_part
    
    return None, None

def topic_mapping (user_input: list):
    for topic in topics:
        if topic in user_input:
            return topic
    return None