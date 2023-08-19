import pandas as pd
df = pd.read_csv('Dataset.csv')
df_with_online_delivery = df[df['Has Online delivery'] == 'Yes']
df_without_online_delivery = df[df['Has Online delivery'] == 'No']
average_rating_with_online_delivery = df_with_online_delivery['Aggregate rating'].mean()
average_rating_without_online_delivery = df_without_online_delivery['Aggregate rating'].mean()
print(f'Average rating for restaurants with online delivery: {average_rating_with_online_delivery:.2f}')
print(f'Average rating for restaurants without online delivery: {average_rating_without_online_delivery:.2f}')
