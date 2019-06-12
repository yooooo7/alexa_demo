import re

intent_mapping = {
    r'.*([^a-z]*overview|[^a-z]*description|[^a-z]*story)': 'askMovieOverview',
    r'.*[^a-z]*review': 'askMovieReview',
    r'.*([^a-z]*release|[^a-z]*date)': 'askMovieReleaseDate',
    r'.*([^a-z]*label|[^a-z]*genre|[^a-z]*category)': 'askMovieLabel',
    r'.*[^a-z]*other (movie|movies)': 'askActorOtherMovies',
    # TODO: can not recognize 'other movie' after key words
    r'((?!other (movie|movies)).)*(actor|star)((?!other (movie|movies)).)*': 'askLeadActor',
    r'.*[^a-z]*suggest': 'suggestMovie',
    r'.*[^a-z]*birth': 'askActorBirthInfo',
    r'.*([^a-z]*biography|[^a-z]*personal statement)': 'askActorBio',
    r'^.*stop conversation$': 'quit'
}

def intentDect(sentence: str):
    for reg in intent_mapping:
        if re.match(reg, sentence):
            return intent_mapping[reg]
    return None