# -*- coding: utf-8 -*-

"""
Lecture 3 - Introduction into AI Programming with Python
@author: Dominik Jung (dominik.jung@jung-isec.de)
"""

# Dataframes with pandas
import pandas as pd
speed = [290, 330, 345]
car = [718, 911, 918]
df = pd.DataFrame()
df["CAR"] = car
df["SPEED"] = speed

df.loc[1:]
df.loc[2]

df.loc[:, 'CAR']
df.loc[1:2, 'CAR':'SPEED']



