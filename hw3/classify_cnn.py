#coding：utf-8
from __future__ import print_function
import json
import random
from sklearn import metrics
import os
import sys
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import f1_score
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Dense, Input, GlobalMaxPooling1D
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model
from keras.initializers import Constant
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model
from keras.optimizers import *
from keras import regularizers
from keras.models import Sequential
MAX_SEQUENCE_LENGTH = 500
MAX_NUM_WORDS = 20000
EMBEDDING_DIM = 100
DATA_SPLIT = 0.1
# pre processing data into label and text
print('Reading dataset')
texts = []  
labels_index = {"facility":0,"environment":1,"location":2,"service":3,"food":4}  
labels = []  
with open('final.json') as json_data:
    data = json.load(json_data)
    corpus = data["corpus"]
random.shuffle(corpus)
for item in corpus:
    texts.append(item["data"])
    labellist = item["label"].split(',')
    temp = []
    for key in labels_index.keys() :
        if key in labellist :
            temp.append(1)
        else :
            temp.append(0)
    labels.append(temp)
# vectorize the text samples into a 2D integer tensor
tokenizer = Tokenizer(num_words=MAX_NUM_WORDS, lower = True)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
labels = np.array(labels)

# split data into train and test
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=DATA_SPLIT, random_state=9000 )
num_words = min(MAX_NUM_WORDS, len(word_index))

#model
model = Sequential()
model.add(Embedding(input_dim=num_words + 1, output_dim=EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH,embeddings_regularizer=regularizers.l2(0.01)))
model.add(Conv1D(128, 5, activation='tanh'))
model.add(MaxPooling1D(5))
model.add(Conv1D(128, 5, activation='tanh'))
model.add(MaxPooling1D(5))
model.add(Conv1D(128, 5, activation='tanh'))
model.add(MaxPooling1D(15))
model.add(Flatten())
model.add(Dense(128, activation='tanh'))
model.add(Dense(len(labels_index), activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['categorical_accuracy'])
# trainning
model.fit(x_train, y_train,nb_epoch=5,batch_size=32,validation_split=0.2)

predicted = model.predict(x_test, batch_size=None, verbose=0, steps=None)
predicted[predicted>=0.4] =1
predicted[predicted<0.4] =0
print("loss:"+str(metrics.hamming_loss(y_test,predicted)))
print("accuracy:"+str(metrics.accuracy_score(y_test,predicted)))
print('F1 score:'+str(f1_score(y_test, predicted, average = 'weighted')))