# -*- coding: utf-8 -*-



#%%
"""
Lecture 3 - Artificial Intelligence Toolbox
"""


d = { "John" : ["alive", "0.5"],
      "Sansa" : ["alive ", "1"],
      "Eddard" : ["dead ", "1"],
      "Bran" : ["alive", "0"],
      "Arya" : ["missing", "1"]
    }

l = [4, 8, 15, 16, 23, 42]

mydict = {'Lagavulin': {'EUR':'16', 'Dollar':'18', 'Pounds':'19'},
	  'The Beast': {'EUR':'25', 'Dollar':'20'}}

mydict["Lagavulin"]
mydict["Lagavulin"]["EUR"]
mydict["Lagavulin"]["EUR"]= 20
mydict["Lagavulin"][0] = 21

import pandas as pd
data = [4, 8, 15, 16, 23, 42]
df = pd.DataFrame(data)
print(df)

#%%
# Exploratory Data Analysis: Bar Chart
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
l = ['Lisp', 'Java', 'GO', 'R','Python']
plt.bar(l, x, align='center')
plt.show()

