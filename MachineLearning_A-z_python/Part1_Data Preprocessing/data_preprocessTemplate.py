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
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
print (X)
Y = dataset.iloc[:,3].values
print ('values of Y')
print (Y)