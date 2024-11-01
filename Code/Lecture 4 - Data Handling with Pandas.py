# -*- coding: utf-8 -*-
"""
Lecture 4 - Data Engineering
@author: Dominik Jung (dominik.jung@jung-isec.de)
"""

import pandas as pd

#%% Create
data = {"Model": ["718", "718","718", "718", "911", "911", "911"],
      "Type": ["Cayman", "Cayman S", "Boxter", "Boxter S", "Carrera", "Carrera 4S", "Targa 4S"],
      "PS": [300, 350, 300, 350, 385, 450, 385],
      "Price":[54900, 67000, 56900, 69000, 103000, 126000, 140000]}

df = pd.DataFrame(data=data, columns=["Type","Model", "PS","Price"])

df
#%% View
df.head()

df.tail()

#%% Insert
df["Wishlist"] = [1,0,0,0,0,1,0]
df

#%% Filter
df["Wishlist"] == 1

df[df["Wishlist"] == 1]

#%% Apply
def calculate_mean(row_col):
    return row_col.mean()

df[["Price","PS"]].apply(calculate_mean, axis=0)
df[["Price","PS"]].apply(calculate_mean, axis=1)  # does it make sense?

#%% Append
new_data = [["Taycan Turbo S", "Taycan", 761, 181000]]
new_row = pd.DataFrame(data=new_data,  columns=["Type","Model", "PS","Price"])
df.append(new_row, ignore_index=True)

#%% Joins
data2 = {"Type" : ["Carrera", "Carrera 4S", "Targa 4S", "Panamera"],
        "Ranking" : [1,2,3,4]}

df2 = pd.DataFrame(data=data2, columns=["Type","Ranking"])

pd.merge(df, df2, on="Type")
pd.merge(df, df2, on="Type", how="inner")
pd.merge(df, df2, on="Type", how="outer")
pd.merge(df, df2, on="Type", how="right")

#%% Group_by
df[["Model","Price","PS"]].groupby("Model").mean()

#%% Sort
df.sort_values(by="PS")

df.sort_values(by="PS", ascending=False)

#%% Data Cleaning
data2 = {"Type" : ["Carrera", "Carrera 4S", "Targa 4S", "Panamera"],
        "Ranking" : [1,2,3,4]}

df2 = pd.DataFrame(data=data2, columns=["Type","Ranking"])
df_new = pd.merge(df, df2, on="Type", how="outer")
df_new.dropna()

#%% fill
df_new.fillna(0)

#%% Rotate
df
df.T

#%% Melt
df["ID"] = [1,2,3,4,5,6,7]

# Single ID
df_melted = pd.melt(df, id_vars=["ID"],
                    value_vars=["PS", "Price"],
                    var_name="Characteristics",
                    value_name="Value")

# Multiple ID vars
df_melted = pd.melt(df, id_vars=["Model","Type"],
                    value_vars=["PS", "Price"],
                    var_name="Characteristics",
                    value_name="Value")
print(df_melted)

#%% Pivot (unmelt)
df_unmelted = df_melted.pivot(index=["ID"], columns=["Characteristics"])

# Reshape
df_unmelted = df_unmelted["Value"].reset_index()
df_unmelted.columns.name = None
print(df_unmelted)

df_melted.pivot_table(index=["Model","Type"], columns=["Characteristics"], values=["Value"])

#%%





