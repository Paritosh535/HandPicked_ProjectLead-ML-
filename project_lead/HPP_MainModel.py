# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:54:22 2017

@author: paritosh.yadav
"""

"""
Created on Thu Oct 12 11:04:04 2017

@author: paritosh.yadav
"""
from .HPPL_PickleFile import load_PickleFile
from .HPP_HPPL_Algo import Train_Test
from collections import Counter


# load data from sales.csv from data

def Predicate(mydata):

    y_top, y_pred = Train_Test(mydata)
    y_pred = [x for x in y_pred if x != y_top]
    empDict = load_PickleFile("Emp")
    listemp = []
    listemp.append(str(int(y_top)) + ' ' + str('Top') + ' ' + empDict[int(y_top)])
    for i, j in Counter((y_pred)).most_common():
        listemp.append(str(int(i)) + ' ' + str(int(j)) + ' ' + empDict[i])

    return listemp[0:5]







