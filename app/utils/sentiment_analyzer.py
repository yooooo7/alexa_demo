from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentimentIntensity_analyzer(text: str) -> str:
    analyser  =  SentimentIntensityAnalyzer()
    results = analyser.polarity_scores(text)
    result = max(results, key = results.get)
    
    return 'other' if (result is not 'pos') and (result is not 'neg') else result