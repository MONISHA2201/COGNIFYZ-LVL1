import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('Dataset.csv')

# Filter for restaurants with ratings
df_filtered = df[df['Aggregate rating'] != 0]

# Group the DataFrame by city and restaurant name
average_ratings = df_filtered.groupby(['City', 'Restaurant Name'])['Aggregate rating'].mean()

# Print the average ratings for each city
for city, restaurant_name, average_rating in average_ratings.iterrows():
    print(f'{city}: {restaurant_name} ({average_rating:.2f}')
