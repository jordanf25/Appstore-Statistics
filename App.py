#import pandas library and read the AppleStore.csv and googleplaystore.csv files into pandas DataFrames
import pandas as pd
df1 = pd.read_csv('/Users/jorda/Downloads/Mobile Appstore Dataset/AppleStore.csv')
df2 = pd.read_csv('/Users/jorda/Downloads/Google Play dataset/googleplaystore.csv')


#expllore the dataframes by printing the first 5 rows and the summary information of each dataframe
print("Apple Store:")
print(df1.head())
print(df1.info())

print("\nGoogle Play Store:")
print(df2.head())
print(df2.info())

#remove any duplicate rows from both dataframes
df1 = df1.drop_duplicates(subset = 'track_name')
df2 = df2.drop_duplicates(subset = 'App')

#filter the dataframes to only include apps that are free
df1 = df1[df1['price'] == 0] 
df2 = df2[df2['Type'] == 'Free']

#find most common genres in both dataframes
df1_genres = df1["prime_genre"].value_counts()
df2_genres = df2["Category"].value_counts()

#find most common genre of Apple Store DataFrame
print("Most common Apple Store genre:", df1_genres.index[0])
print("Most common Google Play Store genre:", df2_genres.index[0])

#find the most popular genre of Apple Store by user ratings by grouping the dataframe by genre and summing the rating counts for each genre
df1_users = df1.groupby("prime_genre")["rating_count_tot"].sum()
print("Most popular Apple Store genre by user ratings:", df1_users.idxmax())
print("Total ratings:", df1_users.max())

#cleaned the Installs column in the Google Play Store DataFrame by removing commas and plus signs and converting the column to an integer data type
df2["Installs"] = (
    df2["Installs"].str.replace(",", "", regex=False).str.replace("+", "", regex=False).astype(int)
)

df2_users = df2.groupby("Category")["Installs"].sum()
print("Most popular Google Play Store genre by total installs:", df2_users.idxmax())
print("Total installs:", df2_users.max())

df1_average = df1.groupby("prime_genre")["rating_count_tot"].mean()

print("Average user ratings for Apple Store genres:", )