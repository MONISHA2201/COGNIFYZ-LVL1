import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Dataset.csv')
df_filtered = df[df['Price range'] != '']
price_ranges = df_filtered['Price range'].tolist()
plt.hist(price_ranges)
plt.xlabel('Price range')
plt.ylabel('Number of restaurants')
plt.title('Distribution of price ranges among restaurants')
plt.show()
