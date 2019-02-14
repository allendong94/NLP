from __future__ import print_function
import json
import os
import sys
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.layers import Dense, Input, GlobalMaxPooling1D
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model
from keras.models import Sequential
from keras.optimizers import SGD
from keras.layers.core import Dense, Dropout, Activation
from sklearn.metrics import f1_score
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding, Flatten, GlobalMaxPool1D, Dropout, Conv1D
from keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from keras.losses import binary_crossentropy
from keras.optimizers import Adam
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import random
from sklearn.model_selection import train_test_split
from sklearn import metrics
from keras.callbacks import Callback
from sklearn.metrics import f1_score, precision_score, recall_score
from keras import regularizers


MAX_SEQUENCE_LENGTH = 500
MAX_NUM_WORDS = 5000

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

tokenizer = Tokenizer(num_words=MAX_NUM_WORDS,lower = True)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
labels = np.array(labels)

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=9000 )

print('Training model.')

model = Sequential()
num_words = min(MAX_NUM_WORDS, len(word_index))
model.add(Embedding(input_dim=num_words + 1, output_dim=100, input_length=MAX_SEQUENCE_LENGTH, embeddings_regularizer=regularizers.l2(0.01)
            ))
model.add(Dropout(0.2))
model.add(Conv1D(128, 5, activation='tanh'))
model.add(GlobalMaxPool1D())
model.add(Dense(len(labels_index)))
model.add(Activation('sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['categorical_accuracy'])


model.fit(x_train, y_train,epochs=20,batch_size=32,validation_split=0.25)

pred = model.predict(x_test)
pred[pred>=0.4] = 1
pred[pred<0.4] = 0
#print (pred)
#print(y_test)
print("loss:"+str(metrics.hamming_loss(y_test,pred)))
print("accuracy:"+str(metrics.accuracy_score(y_test,pred)))
print ('F1 score:'+str(f1_score(y_test, pred, average='weighted')))