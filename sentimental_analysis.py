# -*- coding: utf-8 -*-
"""sentimental analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QqPb5zr5n7BR9TDPU7sXQ7aD5YFsKV5X
"""

import nltk
nltk.download('stopwords')

import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn. linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

pd.read_csv('/content/twitter_training.csv')

columns_name=['id','location','target','text']

df=pd.read_csv('/content/twitter_training.csv', names=columns_name)

df.head()

df['target'].value_counts()

df.shape

"""steeming"""

port_stem = PorterStemmer()

def stemming (content) :

 stemmed_content = re.sub('[^a-zA-Z]',' ', content)
 stemmed_content = stemmed_content.lower()
def stemming (content) :

 stemmed_content = re.sub('[^a-zA-Z]',' ', content)
 stemmed_content = stemmed_content.lower()
 stemmed_content = stemmed_content.split()
 stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
 stemmed_content = ' '.join(stemmed_content)
 return stemmed_content

df['stemmed_content'] = df['text'].apply(stemming)

df.head()

df.dropna(inplace=True)

X = df['stemmed_content'].values
Y = df['target'].values

X

Y

X_train, X_test, Y_train, Y_test = train_test_split(X ,Y , test_size=0.2 , stratify=Y , random_state=2)

X.shape,X_train.shape,X_test.shape

Y.shape,Y_train.shape,Y_test.shape

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print(X_train)

print(X_test)

"""traning ml model logistic regression"""

model = LogisticRegression(max_iter=1000)

model.fit(X_train,Y_train)

X_train_prediction = model.predict(X_train)
traning_data_accuracy = accuracy_score(Y_train , X_train_prediction)

traning_data_accuracy

X_train_prediction

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test , X_test_prediction)

X_test_prediction

test_data_accuracy

"""Model accuracy 77.9%

saving the train model
"""

import pickle

filename = 'train_model.sav'
pickle.dump(model,open(filename,'wb'))

"""using save model for future prediction"""

load_model = pickle.load(open("/content/train_model.sav", 'rb'))

X_new = X_test[800]
print(Y_test[800])

prediction = model.predict(X_new)
print("Prediction of new data is :",prediction)

