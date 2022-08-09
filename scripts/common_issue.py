import pandas as pd

# first level classification number and classication of percentage
df = pd.read_csv('data.csv')
classify_type = 'Classification'
total = pd.DataFrame({'total': df.groupby(classify_type).size()})
total = total.sort_values(['tostal'], ascensding=False)
total['2'] = total['total']
total['total'] = total['total'].map(lambda x: x / 10)
print(total)

