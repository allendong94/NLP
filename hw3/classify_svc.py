import tensorflow as tf
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
import sys
import os
from sklearn.metrics import f1_score
import random
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm
from sklearn.pipeline import Pipeline
from sklearn import metrics
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import warnings
warnings.filterwarnings("ignore")

samples = []
labels = []
# open a file from the path
file = open("final.json", "r")
out = file.read()
filejs = json.loads(out)
corpus = filejs["corpus"]
perc_train = 0.8
random.shuffle(corpus)
# pre-processing data into label and text
print('Reading dataset')
for item in corpus:
    samples.append(item["data"])
    labellist = item["label"].split(',')
    labels.append(labellist)
n_samples = len(samples)
index_split = int(perc_train*n_samples)
train_samples = samples[0:index_split]
train_labels = labels[0:index_split]
test_samples = samples[index_split+1:n_samples]
test_labels = labels[index_split+1:n_samples]

#linear SVC /Linear Support Vector Classification
classifier = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', OneVsRestClassifier(LinearSVC()))])
classifier.fit(train_samples, train_labels)

predicted = classifier.predict(test_samples)
print("loss:"+str(metrics.hamming_loss(test_labels,predicted)))
print("accuracy:"+str(metrics.accuracy_score(test_labels,predicted)))
print('F1 score:'+str(f1_score(test_labels, predicted, average = 'weighted')))