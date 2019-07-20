#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:02:56 2019

@author: hyadala
"""

#DataPreprocessing

#importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
#X-independent variable ,Y-Dep variable
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
print (X)
Y = dataset.iloc[:,3].values
print ('values of Y')
print (Y)

#Taking care of missing data using scikit library
print('Taking care of missing data using scikit library')
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values=  'NaN' ,strategy="mean",axis=0)
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
print (X)

