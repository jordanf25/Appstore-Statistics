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

print(df1_genres)