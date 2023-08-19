import pandas as pd
df = pd.read_csv('Dataset.csv')
df_filtered = df[df['Aggregate rating'] != 0]
average_ratings = df_filtered.groupby('City')['Aggregate rating'].mean()
highest_average_rating_city = average_ratings.idxmax()
print(f'The city with the highest average rating is {highest_average_rating_city}.')
