from ..utils import sentimentIntensity_analyzer
from .normalization import normalization
from .mapping import mapping

def user_sentiment(input: str) -> str:
    return sentimentIntensity_analyzer(input)

def NLU(sentence: str):
    # sentiment analysis
    sentiment = user_sentiment(sentence)

    # normalization
    normalized_sentence = normalization(sentence)

    # mapping
    entity = mapping(normalized_sentence)

    return entity, sentiment
