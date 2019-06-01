from ..utils import sentimentIntensity_analyzer
from .normalization import normalization
from .mapping import mapping
from .mapping import topic_mapping

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

def topic_detection(sentence: str):
    # normalization
    normalized_sentence = normalization(sentence)
    # topic mapping
    topic = topic_mapping(normalized_sentence)
    return topic