from .summarizers import lexRank_summarizer
from ..utils import sentimentIntensity_analyzer
from .template.movie import MOVIE_TEMPLATE
from .dialogGraph import *

# using movie title to get a pd.dataframe of reviews, summaries and sentiments
def movie_reviews_summarise_sentiment(movie_title: str, reviews: list, summarizer, summary_max_length: int, analyzer) -> list:
    """
    Arguments:
    movie title -- movie title for search
    summarizer -- a predefined summarizer to summarize
    summary_max_length -- based on summarizer, it could be the number of words or sentences of summary
    analyzer -- sentiment analyzer
    
    Returns:
    pd.DataFrame of reviews, sentiments, summarise and titles for one movie
    """
    result = []
    
    # for each reviews, genearte summary and it's sentiment
    for review in reviews:
        summary = summarizer(review, summary_max_length)
        sentiment = analyzer(review)
        result.append({ 
            'title': movie_title,
            'review': review,
            'summary': summary,
            'sentiment': sentiment
        })
    
    return result