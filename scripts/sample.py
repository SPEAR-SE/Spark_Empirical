import pandas as pd
from pandas import DataFrame

df = pd.read_csv('raw_data.csv')
df = df[df['Body'].str.contains('<code>')]
df['date'] = pd.to_datetime(df['CreationDate'])
df = df.set_index('date')
print(len(df))
df = df['2014':'2019']
print(len(df))
sample = DataFrame.sample(df, n=1000, replace=False)
sample.to_csv('result.csv')
