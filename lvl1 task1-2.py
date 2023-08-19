import pandas as pd
df = pd.read_csv('Dataset.csv')
cuisine_counts = df.groupby('Cuisines').size()
total_restaurants = len(df)
cuisine_percentages = cuisine_counts / total_restaurants * 100
top_three_cuisines = cuisine_counts.head(3)
for cuisine, percentage in zip(top_three_cuisines.index, cuisine_percentages):
 print(f'{cuisine}: {percentage:.2f}%')
