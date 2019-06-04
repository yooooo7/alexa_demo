import re
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

def normalization(sentence):
    #1. lower case
    sentence = sentence.lower()
    
    #2. removing punctuation
    ntokens = nltk.word_tokenize(sentence)
    normalized_sentence = []
    for string in ntokens:
        tokens = re.sub(r"[^a-z0-9]+", " ", string.lower())
        normalized_sentence.append(tokens)
    
    #3. stemming
    stemmer = PorterStemmer()
    stemmed_sentence = []
    for word in normalized_sentence:
        stemmed_sentence.append(stemmer.stem(word))
    
    #4. lemmatization
    lemmatized_sentence = []
    lemmatizer = WordNetLemmatizer()
    for word in normalized_sentence:
        lemmatized_sentence.append(lemmatizer.lemmatize(word))
    
    # remove ' '
    for _ in range(lemmatized_sentence.count(' ')):
        lemmatized_sentence.remove(' ')
    
    # stopword removal
    stop_words = set(stopwords.words('english'))
    removal_sentence = [i for i in lemmatized_sentence if not i in stop_words]

    return removal_sentence