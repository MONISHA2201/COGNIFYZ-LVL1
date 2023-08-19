import pandas as pd
df = pd.read_csv('Dataset.csv')
df_filtered = df[df['Price range'] != '']
price_ranges = df_filtered['Price range'].value_counts().keys().tolist()
number_of_restaurants_per_price_range = df_filtered['Price range'].value_counts().tolist()
total_number_of_restaurants = len(df_filtered)
percentage_of_restaurants_per_price_range = []
for i in range(len(price_ranges)):
    percentage_of_restaurants_per_price_range.append(
        number_of_restaurants_per_price_range[i] / total_number_of_restaurants * 100)
print(f'Percentage of restaurants in each price range:')
for i in range(len(price_ranges)):
    print(f'{price_ranges[i]}: {percentage_of_restaurants_per_price_range[i]:.2f}%')
