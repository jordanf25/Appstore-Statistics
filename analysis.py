#import pandas library and read the AppleStore.csv and googleplaystore.csv files into pandas DataFrames
import pandas as pd
df1 = pd.read_csv('/Users/jorda/Downloads/Mobile Appstore Dataset/AppleStore.csv')
df2 = pd.read_csv('/Users/jorda/Downloads/Google Play dataset/googleplaystore.csv')


#explore the dataframes by printing the first 5 rows and the summary information of each dataframe
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

#built a function to clean the Installs column in a dataframe and converting the column to an integer data type, then call it on the Google Play Store (df2) dataframe
def clean_installs(df):
    df["Installs"] = (
        df["Installs"]
        .str.replace(",", "", regex=False)
        .str.replace("+", "", regex=False)
        .astype(int)
    )
    
    return df

df2 = clean_installs(df2)

#find the most popular genre of Google Play Store by total installs by grouping the dataframe by genre and summing the installs for each genre
df2_users = df2.groupby("Category")["Installs"].sum()
print("Most popular Google Play Store genre by total installs:", df2_users.idxmax())
print("Total installs:", df2_users.max())

#find highest average number of user ratings for Apple Store genres by grouping the dataframe by genre and calculating the mean of the rating counts for each genre
df1_average = df1.groupby("prime_genre")["rating_count_tot"].mean()

print("Average user ratings for Apple Store genres:")
print(df1_average.sort_values(ascending=False))

print("Apple genre with highest average ratings:", df1_average.idxmax())
print("Highest average ratings:", df1_average.max())

#find average Installs for Google Play store genres by grouping the dataframe by genre and calculating the mean of the installs for each genre
df2_average = df2.groupby("Category")["Installs"].mean()
print("Average installs for Google Play Store genres:", df2_average.sort_values(ascending=False))
print("Google Play genre with highest average installs:", df2_average.idxmax())
print("Highest average installs:", df2_average.max())

#Google Play Statistics table

category_stats = df2.groupby("Category").agg(
    app_count=("App", "count"),
    total_installs=("Installs", "sum"),
    average_installs=("Installs", "mean")
)

print("\nGoogle Play Store Category Statistics:")
print(category_stats.sort_values(by="average_installs", ascending=False))

#Apple Store Statistics table
apple_stats = df1.groupby("prime_genre").agg(
    app_count=("track_name", "count"),
    total_ratings=("rating_count_tot", "sum"),
    average_ratings=("rating_count_tot", "mean")
)

print("\nApple Store Genre Statistics:")
print(apple_stats.sort_values(by="average_ratings", ascending=False))

#final recommendations based on the analysis of the dataframes
print("\n-----RECOMMENDATIONS-----")

print("App Store Recommendation:")
print("Based on this analysis, the best app to develop is a " + df1_average.idxmax() + " app because this genre has the highest average number of ratings per app. A higher number of ratings suggests that apps in this genre attract substantial user activity, which could provide greater potential for advertising revenue.")
print("\nGoogle Play Store Recommendation:")
print("Based on this analysis, the best app to develop is a " + df2_average.idxmax().title() + " app because this genre has the highest average number of installs per app. A higher average number of installs suggests that apps in this genre have strong potential to attract users, which could provide greater potential for advertising revenue.")