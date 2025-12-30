import pandas as pd 
import numpy as np
import re 
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def clean(doc):
    # doc is a string of text
    # let's define a regex to match special characters and digits
    regex = '[^a-zA-Z.]'
    doc = re.sub(regex, ' ', doc)
    # convert to lowercase
    doc = doc.lower()
    # tokenization
    tokens = nltk.word_tokenize(doc)
    # Stop word removal 
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # join and return 
    return ' '.join(lemmatized_tokens)
