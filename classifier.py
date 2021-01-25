import re


def preprocess_text(x, lemmatizer):
    """
    Lemmatize words and remove unnecessary characters
    :param x: list of sentences in an article
    :param lemmatizer: object with lemmatization method (for example, Mystem)
    :return: string containing preprocessed text
    """
    x = " ".join(x)
    x = re.sub('[^А-Яа-яA-Za-z0-9]+', ' ', x)
    x = [lemmatizer.lemmatize(i)[0] for i in x.split()]
    x = " ".join(x)
    return x


def vectorize_text(x, vectorizer):
    """
    Get numerical characteristics of the input text
    :param x: preprocessed text
    :param vectorizer: object for text vectorization (like TfidfVectorizer or CountVectorizer)
    :return: 1-d feature vector
    """
    x = vectorizer.transform([x])
    return x


def make_prediction(x, model):
    """
    Classify text into one of 2 categories - world news or Russian news
    :param x: preprocessed and vectorized text
    :param model: pretrained classifier with 'predict' method
    :return: string containing predicted category
    """
    pred = model.predict(x)
    if pred == 0:
        return "World"
    else:
        return "Russia"

