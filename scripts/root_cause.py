import pandas as pd

#get the percentage for root causess
df = pd.read_csv('data.csv')
#filter the types that we dont need
nouse_second=['Serialization', 'Logging', 'Other', 'Spark Bug']
df = df[(True ^ df['Classification'].isin(nouse_second))]
print(len(df))
# get the percentage for root cause
classify_type = 'Root Cause'
total = pd.DataFrame({'total': df.groupby(classify_type).size()})
total = total.sort_values(['total'], ascending=False)
total['number'] = total['total']
count = total['number'].sum()
print(count)
total['total'] = total['total'].map(lambda x: x / count).round(3)
print(total)