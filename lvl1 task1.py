import pandas as pd
df = pd.read_csv('Dataset.csv')
cuisine_counts = df.groupby('Cuisines').size()
cuisine_counts = cuisine_counts.sort_values(ascending=False)
top_three_cuisines = cuisine_counts.head(3)
print(top_three_cuisines)
