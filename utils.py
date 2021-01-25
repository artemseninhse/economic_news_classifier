import pickle


BATCH_SIZE = 20
MAX_SLEEP = 3
VECTORIZER = "tfidf.pkl"
MODEL = "logreg_baseline.pkl"
STR_TO_REMOVE = [" :: Экономика :: РБК", " :: Политика :: РБК"]


def load_pickle(path):
    """
    Load serialized object
    :param path: path to file
    :return: object
    """
    return pickle.load(open(path, "rb"))


def dump_pickle(file, path):
    """
    Serialize Python object
    :param file: object to serialize
    :param path: path to serialized file
    :return: None
    """
    pickle.dump(file, open(path, "wb"))

