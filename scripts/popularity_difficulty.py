import pandas as pd

#count the median or mean value
df = pd.read_csv('data.csv')
print(len(df))
classify_type = 'Classification'
df = df.groupby(classify_type).mean().round(1)
#df = df.groupby(classify_type).median().round(1)
pd.set_option('display.max_columns', None)
df.to_csv("results.csv")
print(df)