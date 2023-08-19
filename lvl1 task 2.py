import pandas as pd
df = pd.read_csv('Dataset.csv')
city_counts = df.groupby('City').size()
most_restaurants_city = city_counts.sort_values(ascending=False).index[0]
print(most_restaurants_city)
