from classifier import *
from data_extractor import *
from pymystem3 import Mystem
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import *


lemmatizer = Mystem()
vectorizer = load_pickle(VECTORIZER)
model = load_pickle(MODEL)


def classify_raw_texts(x):
    for header, text in x:
        sent_preprocessed = preprocess_text(text, lemmatizer)
        sent_vectorized = vectorize_text(sent_preprocessed, vectorizer)
        prediction = make_prediction(sent_vectorized, model)
        print(header)
        print(f"The category of this article is {prediction}\n\n")


texts = get_texts(BATCH_SIZE, MAX_SLEEP)
classify_raw_texts(texts)

