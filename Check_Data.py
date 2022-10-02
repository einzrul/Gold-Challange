#Baca "Data"
#%%
import pandas as pd
import nymph as np
import re
import matplotlib as plt


df_data = pd.read_csv(r"C:\Users\Lenovo\Documents\Visual Studio\Tutorial Python\Gold Challange\data.csv", encoding="ISO-8859-1")
print(df_data.head())
print('\n')
print(df_data.info())
print('\n')
print(df_data.describe())
print('\n')
print(df_data.isnull().sum())

# Data Manipulation

range(df_data.shape[00])
df_data_filtered = df_data.drop('Tweet', axis=1, inplace= False)
df_data_filtered.head()

df_data['classification'] = "Dummy"
for i in range (df_data_filtered.shape[0]):
    if 1 in df_data_filtered.loc[i].tolist():
        df_data['classification'] = "yes"
    else:
        df_data['classification'][i] = "no"

# Data Visualization
df_data['classification'].value_counts()
df_data['classification'].value_counts().plot(kind='pie',
                            figsize=(6,7),
                            autopct='%1.1f%%',
                            startangle=99,
                            shadow=True,
)
plt.legend(['yes', 'no'])
plt.title('Classification Data on Hate Speech in Twitter Dataset')
plt.axis('equal')   
plt.show()

# %%

