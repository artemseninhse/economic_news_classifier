## Economic News Classifier

![Example](example.png)

This program classifies 20 latest news from rbk.ru into 2 categories - foreign news (World) and Russian news (Russia).

### Steps

1. Parsing the text of 20 latest news from rbk.ru
2. Text preprocessing which includes lemmatization and deleting special characters
3. Text vectorization using pretrained TFIDF
4. Text classification using pretrained Logistic Regression classifier

### How to launch
```
$ git clone https://github.com/artemseninhse/economic_news_classifier.git
$ cd economic_news_classifier/
$ docker build -t economic_news_classifier .
$ docker run economic_news_classifier
```

