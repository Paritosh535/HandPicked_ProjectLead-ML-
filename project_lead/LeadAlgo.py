import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle as pkl



dataset = pd.read_excel("df.xls", encoding='utf-8')
datasetemp = pd.read_csv('Employee.csv', low_memory=False)
datasetemp = datasetemp.iloc[:, [0, 1, 3]]

empDict = {}
for i in range(len(datasetemp)):
    empDict.__setitem__(datasetemp['fld_empId'][i],
                        ((str(datasetemp['fld_empFirstName'][i]) + ' ' + str(datasetemp['fld_empLastName'][i]))))

df = dataset.dropna()  # drop row NaN
# df=df.loc[df['salesperson_id'] != 326] #select rows as per condition
df = df.reset_index(drop=True)  ##vertical index
df = df.iloc[:, [0, 2]]

# dataset process for NLP Cleaning Stopword and Stemmer
# corpus= []
# for i in range(len(df)):
#    review = re.sub('[^a-zA-Z]', ' ', df['understanding'][i])
#    review = review.lower()
#    review = review.split()
#    ps = PorterStemmer()
#    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
#    review = ' '.join(review)
#    corpus.append(review)
#
##make Pickle file
# save_documents=open("corpus.pickle","wb")
# pkl.dump(corpus,save_documents)
# save_documents.close()

# load pikle file
documents_open = open("corpus.pickle", "rb")
corpus = pkl.load(documents_open)
documents_open.close()

length_corpus = (len(corpus))
st = "The proposed app is for a cab agency. Drivers have Android phones,who get push notifications from customers and provides service to its customers on receipt of requests. Any customer who is logged on to the app,can find a nearby cab of the particular agen"

datacorpus = []
review = re.sub('[^a-zA-Z]', ' ', st)
review = review.lower()
review = review.split()
ps = PorterStemmer()
review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
review = ' '.join(review)

corpus.append(review)
for x in set(review.split()):
    corpus.append(x)

# abc=corpus[length_corpus:len(corpus)]
# print(len(corpus)+len(datacorpus))
# print(corpus[len(corpus):len(datacorpus)])

# Create sparsh Matric of Corpus
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=2500)
X = cv.fit_transform(corpus).toarray()
y = df.iloc[:, 1].values

my = X[length_corpus:len(corpus)]

# print(cv.inverse_transform(X[5718:5719]))
# print(cv.inverse_transform(my))

corpus = corpus[0:length_corpus]
X = X[0:length_corpus]

from sklearn.naive_bayes import GaussianNB

GNB = GaussianNB()
# GNB.fit(X_train, y_train)

GNB.fit(X, y)
# print(GNB.score(X_train, y_train))
# Predicting the Test set results
y_pred = GNB.predict(my)

from collections import Counter

listemp = []
listemp.append(str(int(y_pred[0])) + ' | ' + str('Top') + ' | ' + empDict[int(y_pred[0])])
for i, j in Counter(y_pred[1:]).most_common():
    listemp.append(str(int(i)) + ' | ' + str(int(j)) + ' | ' + empDict[i])





