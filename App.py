#import pandas library and read the AppleStore.csv and googleplaystore.csv files into pandas DataFrames
import pandas as pd
df1 = pd.read_csv('/Users/jorda/Downloads/Mobile Appstore Dataset/AppleStore.csv')
df2 = pd.read_csv('/Users/jorda/Downloads/Google Play dataset/googleplaystore.csv')

#print(df1.head())
#print(df1.info())

#combine the two DataFrames into a single DataFrame and remove any duplicate rows, then reset the index of the final DataFrame
combined_df = pd.concat([df1, df2])
final_df = combined_df.drop_duplicates().reset_index(drop=True)
colums_to_show = ['track_name', 'price', 'Genres']

free_df = final_df.loc[final_df['price'] == 0].copy()
#print(free_df[colums_to_show].head(10))

free_df['installs_clean'] = free_df['Installs'].astype(str).str.replace('+', '', regex=False)
free_df['installs_clean'] = free_df['installs_clean'].str.replace(',', '', regex=False)
free_df['installs_clean'] = pd.to_numeric(free_df['installs_clean'], errors='coerce')


# Step 2: Calculate the average (mean) installs for each genre
genre_avg_installs = free_df.groupby('Genres')['installs_clean'].mean()

# Step 3: Get the top 5 genres by average installs
top_5_genres = genre_avg_installs.nlargest(5)

print("Top 5 Genres by Average Installs:")
print(top_5_genres)
