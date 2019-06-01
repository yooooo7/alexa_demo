from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentimentIntensity_analyzer(text: str) -> str:
    analyser  =  SentimentIntensityAnalyzer()
    result = analyser.polarity_scores(text)
    return max(result, key = result.get)