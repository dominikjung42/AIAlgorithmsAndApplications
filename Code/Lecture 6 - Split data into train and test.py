# -*- coding: utf-8 -*-
"""
Lecture 6 - Silhouette Coefficient.py
@author: Dr. Dominik Jung
"""

#%%
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

X, y = datasets.load_iris(return_X_y=True)

#%%
from sklearn.model_selection import cross_val_score
clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, X, y, cv=5)
scores