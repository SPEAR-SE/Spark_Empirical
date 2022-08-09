import pandas as pd

df = pd.read_csv('data_with_date.csv')
df['questionCreateDate'] = pd.to_datetime(df['questionCreateDate'])
df['year'] = df['questionCreateDate'].dt.year
df['diff'] = 2019 - df['year'] + 1
print(df)
df['normalized_view'] = df['ViewCount'] / df['diff']
classify_type = 'Classification'
df = df.groupby(classify_type).mean().round(1)
df = df.sort_values(['normalized_view'], ascending=False)
print(df)