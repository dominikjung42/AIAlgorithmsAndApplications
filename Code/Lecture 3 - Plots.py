# -*- coding: utf-8 -*-

"""
Lecture 3 - Introduction into AI Programming with Python
@author: Dominik Jung (dominik.jung@jung-isec.de)
"""

# Exploratory Data Analysis: Bar Chart
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
l = ['Lisp', 'Java', 'GO', 'R','Python']
plt.bar(l, x, align='center')
plt.show()
