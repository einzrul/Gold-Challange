#Baca Dataset "New Kamus Alay"
import pandas as pd
import nymph as np
import re
import matplotlib as plt

df_alay = pd.read_csv(r"C:\Users\Lenovo\Documents\Visual Studio\Tutorial Python\Gold Challange\new_kamusalay.csv", encoding="ISO-8859-1")

print(df_alay.head())
print('\n')
print(df_alay.info())
print('\n')
print(df_alay.describe())
print('\n')
print(df_alay.isnull().sum())