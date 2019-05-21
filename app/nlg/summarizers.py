from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser 
from sumy.summarizers.lex_rank import LexRankSummarizer
import math
import numpy as np

# generate a percentage of max number of words or sentences
def summary_ratio(text:str) -> float:
    text_length = 0.001 * len(text)
    return 1. / (1. + np.exp(-text_length))

# generate a number of word count or sentence count
def summary_count(text: str, max_length: int) -> int:
    ratio = summary_ratio(text)
    return math.ceil(ratio * max_length)

# genearte summary from a text using lexRank summarizer
def lexRank_summarizer(text: str, sentences: int) -> object:
    """
    Arguments:
    text -- a string for summarize
    sentences -- sentences number of summary
    
    Returns:
    a string of summary
    """
    # init model
    language = 'english'
    stemmer = Stemmer(language)
    summarizer = LexRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    
    # parsing text
    parser = PlaintextParser(text, Tokenizer(language))
    
    # generate summary
    summary = [ str(sentence) for sentence in summarizer(parser.document, sentences) ]
    
    return " ".join(summary)