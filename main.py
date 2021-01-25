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
    """
    Determine category of the text (world news or Russian news)
    :param x: text parsed from rbk.ru
    :return: string containing predicted category
    """
    world_news = []
    russian_news = []
    for header, text in x:
        sent_preprocessed = preprocess_text(text, lemmatizer)
        sent_vectorized = vectorize_text(sent_preprocessed, vectorizer)
        prediction = make_prediction(sent_vectorized, model)
        if prediction == "World":
            world_news.append(header)
        else:
            russian_news.append(header)
    print("МЕЖДУНАРОДНЫЕ НОВОСТИ:")
    print("\n".join(world_news))
    print("\nРОССИЙСКИЕ НОВОСТИ:")
    print("\n".join(russian_news))

texts = get_texts(BATCH_SIZE, MAX_SLEEP)
classify_raw_texts(texts)

