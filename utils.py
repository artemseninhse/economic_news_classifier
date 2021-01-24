import pickle


BATCH_SIZE = 20
MAX_SLEEP = 3
VECTORIZER = "tfidf.pkl"
MODEL = "logreg_baseline.pkl"
STR_TO_REMOVE = [" :: Экономика :: РБК", " :: Политика :: РБК"]


def load_pickle(path):
    return pickle.load(open(path, "rb"))


def dump_pickle(file, path):
    pickle.dump(file, open(path, "wb"))

