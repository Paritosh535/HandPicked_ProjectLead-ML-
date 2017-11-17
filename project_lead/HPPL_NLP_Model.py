# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:44:59 2017

@author: paritosh.yadav
"""
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from .HPPL_PickleFile import load_PickleFile


def NLP_Process(data):
    #    dataset process for NLP Cleaning Stopword and Stemmer
    corpus = []
    for i in range(len(data)):
        review = re.sub('[^a-zA-Z]', ' ', data['understanding'][i])
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        corpus.append(review)
    return corpus


def NLP_Cleaning_Add_to_Corpus(mytext):
    text = ''.join(str(e) for e in mytext)
    load_corpus_X = load_PickleFile("corpus_X")
    load_corpus_y = load_PickleFile("corpus_y")
    length_corpus_X = (len(load_corpus_X))
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    load_corpus_X.append(review)  # top Result whole data
    for x in set(review.split()):
        load_corpus_X.append(x)

    return load_corpus_X, load_corpus_y, length_corpus_X

