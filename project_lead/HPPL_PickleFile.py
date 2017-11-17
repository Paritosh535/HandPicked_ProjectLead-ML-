# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:36:59 2017

@author: paritosh.yadav
"""

import pickle as pkl
import pandas as pd
import sys


def make_PickleFile(data, filename):
    try:
        save_documents = open("D:/Github/HPPL/project_lead/PickleFile/" + filename + ".pickle", "wb")
        pkl.dump(data, save_documents)
        save_documents.close()
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    return "success file name is " + filename


def load_PickleFile(filename):
    data = pd.DataFrame({})
    try:
        documents_open = open("D:/Github/HPPL/project_lead/PickleFile/" + filename + ".pickle", "rb")
        file = pkl.load(documents_open)
        documents_open.close()
        data = file
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    return data
