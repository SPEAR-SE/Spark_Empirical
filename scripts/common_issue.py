import pandas as pd

# get classification number and classication of percentage
df = pd.read_csv('data.csv')
classify_type = 'Classification'
total = pd.DataFrame({'number': df.groupby(classify_type).size()})
total = total.sort_values(['number'], ascending=False)
total['percentage'] = total['number'].map(lambda x: x / 10)
print(total)

