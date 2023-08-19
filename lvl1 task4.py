import pandas as pd
df = pd.read_csv('Dataset.csv')
df_filtered = df[df['Has Online delivery'] == 'Yes']
number_of_restaurants_with_online_delivery = len(df_filtered)
total_number_of_restaurants = len(df)
percentage_of_restaurants_with_online_delivery = number_of_restaurants_with_online_delivery / total_number_of_restaurants * 100
print(f'Percentage of restaurants with online delivery: {percentage_of_restaurants_with_online_delivery:.2f}%')
