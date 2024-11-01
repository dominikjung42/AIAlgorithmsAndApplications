# -*- coding: utf-8 -*-
"""
Lecture 4 - Introduction into AI Programming with Python
@author: Dominik Jung (dominik.jung@jung-isec.de)
"""
#%%
import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3]
y = [0, 60000, 80000, 100000]
plt.plot(x,y)

plt.axis([0, 5, 0, 120000])
plt.title("Very nice pic of my future income as AI Specialist")
plt.xlabel("Job years")
plt.ylabel("Yearly income in €")
 
plt.show()


#%%
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
l = ['Lisp', 'Java', 'GO', 'R','Python']
plt.bar(l, x, align='center')
plt.show()

#%%
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = [100, 22, 38, 14, 59, 7, 48, 20]
num_bins = 3
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()
