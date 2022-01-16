# -*- coding: utf-8 -*-
"""
Lecture 6 - Silhouette Coefficient.py
@author: Dr. Dominik Jung
"""

#%%
from numpy import array
from sklearn.datasets import load_iris
from sklearn import tree

# our car data sample from lecture with numeric encoded features
# price(1 = small, 2 = medium, 3 = high),
# maintenance (1 = cheap, medium = 2, expensive = 3)
# number_doors (1,2,3,4,5)
# class, buy (1 = buy, 0 = no buy)

X = array([[1, 1, 3],
       [3, 3, 5],
       [1, 2, 5],
       [2, 3, 2]])

Y = array([1, 0, 1, 0])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

tree.plot_tree(clf) 

