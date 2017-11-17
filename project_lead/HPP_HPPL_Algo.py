# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:53:52 2017

@author: paritosh.yadav
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from .HPPL_NLP_Model import NLP_Cleaning_Add_to_Corpus


def Train_Test(mytext):
    corpus_X, corpus_y, length = NLP_Cleaning_Add_to_Corpus(mytext)
    cv = CountVectorizer(max_features=2000)  # cv = CountVectorizer(max_features=2500)
    X = cv.fit_transform(corpus_X).toarray()
    y = corpus_y
    mytext = X[length:len(corpus_X)]
    X = X[0:length]
    GNB = GaussianNB()
    GNB.fit(X, y)
    y_pred = GNB.predict(mytext)

    return y_pred[0], y_pred