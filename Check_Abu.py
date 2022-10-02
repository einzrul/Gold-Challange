import pandas as pd
import nymph as np
import re
import matplotlib as plt

#Baca Dataset "Abusive"

df_abusive = pd.read_csv(r"C:\Users\Lenovo\Documents\Visual Studio\Tutorial Python\Gold Challange\abusive.csv", encoding="ISO-8859-1")
print(df_abusive.head())
print('\n')
print(df_abusive.info())
print('\n')
print(df_abusive.describe())
print('\n')
print(df_abusive.isnull().sum())