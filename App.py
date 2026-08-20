#import pandas library and read the AppleStore.csv and googleplaystore.csv files into pandas DataFrames
import pandas as pd
df1 = pd.read_csv('/Users/jorda/Downloads/Mobile Appstore Dataset/AppleStore.csv')
df2 = pd.read_csv('/Users/jorda/Downloads/Google Play dataset/googleplaystore.csv')

print("Apple Store:")
print(df1.head())
print(df1.info())

print("\nGoogle Play Store:")
print(df2.head())
print(df2.info())

