import re


def preprocess_text(x, lemmatizer):
    x = " ".join(x)
    x = re.sub('[^А-Яа-яA-Za-z0-9]+', ' ', x)
    x = [lemmatizer.lemmatize(i)[0] for i in x.split()]
    x = " ".join(x)
    return x


def vectorize_text(x, vectorizer):
    x = vectorizer.transform([x])
    return x


def make_prediction(x, model):
    pred = model.predict(x)
    if pred == 0:
        return "World"
    else:
        return "Russia"

