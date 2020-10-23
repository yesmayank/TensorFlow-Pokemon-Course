import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

df = pd.read_csv('./resources/pokemon_alopez247.csv')
# print(df.columns)
# filter the information to be used.
df = df[['Name','isLegendary','Generation', 'Type_1', 'Type_2', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed','Color','Egg_Group_1','Height_m','Weight_kg','Body_Style']]
# print(df.columns)
# Convert the datatype of columns in which possible
df['isLegendary'] = df['isLegendary'].astype(int)
print(df)
# normalize categories.
def dummy_creation(df, dummy_categories):
    for i in dummy_categories:
        df_dummies = pd.get_dummies(df[i])
        df = pd.concat([df, df_dummies], axis = 1)
        df = df.drop(i, axis = 1)
    return df
df = dummy_creation(df, ['Egg_Group_1', 'Body_Style', 'Color','Type_1', 'Type_2'])
print(df)