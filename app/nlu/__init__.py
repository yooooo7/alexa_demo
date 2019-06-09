from ..utils import sentimentIntensity_analyzer
from .normalization import normalization
from .ner import mapping, dic
from .intentClassification import intentDect

def user_sentiment(input: str) -> str:
    return sentimentIntensity_analyzer(input)

def NLU(sentence: str):
    # sentiment analysis
    sentiment = user_sentiment(sentence)

    # normalization
    normalized_sentence = normalization(sentence)
    
    # NER
    entity = mapping(normalized_sentence)
    
    # intent classification
    intent = intentDect(sentence)

    return { 'sentiment': sentiment, 'entity': entity, 'intent': intent }