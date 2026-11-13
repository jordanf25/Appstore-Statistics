Apple App Store & Google Play Store Analysis
Project Overview
This project uses Python and pandas to explore free mobile apps on the
Apple App Store and Google Play Store. The goal is to compare app
categories, measure user engagement, and identify categories that may
offer opportunities for an app supported by advertising revenue.

The analysis focuses on: - The most common app genres and categories on
each platform. - Apple App Store genres with the highest total and
average number of user ratings. - Google Play Store categories with the
highest total and average number of installs. - Category-level
statistics, including app counts and engagement measures. -
Data-informed recommendations for potential app development.
Tools and Technologies
- Python
- pandas
- Jupyter Notebook or a Python environment (for running the
  analysis)
Datasets
The script expects two CSV files:
1. AppleStore.csv --- Apple App Store app data.
2. googleplaystore.csv --- Google Play Store app data.
Place both files in your project directory, or update the file paths in
analysis.py to match their locations. The datasets are not included in
this repository.
Analysis Workflow
1. Load and inspect the data
The script loads both CSV files into pandas DataFrames and displays the
first five rows and summary information for each dataset.
2. Clean the data
- Removes duplicate Apple apps using the track_name column.
- Removes duplicate Google Play apps using the App column.
- Filters both datasets to include free apps only.
- Cleans the Google Play Installs column by removing commas and plus
  signs, then converts it to an integer.
3. Explore app categories
The analysis counts apps in each Apple genre and Google Play category to
identify the most common categories on each platform.
4. Measure user engagement
For the Apple App Store, the script groups apps by prime_genre and
calculates total and average user rating counts.

For Google Play, it groups apps by Category and calculates total and
average installs.
5. Create category-level statistics
The script produces summary tables for both platforms:

Google Play Store - Number of apps in each category - Total
installs - Average installs per app

Apple App Store - Number of apps in each genre - Total user
ratings - Average user ratings per app
6. Make recommendations
The final section identifies: - The Apple genre with the highest average
number of user ratings. - The Google Play category with the highest
average number of installs.

These measures are used as indicators of potential user reach and
possible advertising opportunities.
How to Run
1. Clone or download this repository.
2. Make sure Python is installed.
3. Install pandas:
   pip install pandas
4. Put AppleStore.csv and googleplaystore.csv in the project
   directory.
5. Update the CSV paths near the top of analysis.py if needed. For
   example, if the files are in the same directory as the script:
   df1 = pd.read_csv("AppleStore.csv")
   df2 = pd.read_csv("googleplaystore.csv")
6. Run the script:
   python analysis.py
The results, category summaries, and recommendations will be printed in
the terminal.
Key Files
.
├── analysis.py
├── AppleStore.csv          # Add locally; not included
├── googleplaystore.csv     # Add locally; not included
└── README.md
Limitations
- The analysis uses rating counts and install counts as indicators of
  engagement; these measures do not directly represent active users,
  retention, or revenue.
- A category's average can be affected by the number and distribution
  of apps in that category.
- The recommendations are exploratory. They do not account for
  development costs, competition, monetization rates, or the
  likelihood that a new app will succeed.
- The results depend on the versions and quality of the source
  datasets.
Future Improvements
- Visualize category comparisons with charts.
- Compare app ratings as well as rating counts.
- Investigate competition and pricing across categories.
- Add revenue estimates using clearly stated advertising assumptions.
- Improve data validation and handle missing or unexpected values.
This project was completed as a data analysis exercise using publicly
available mobile app store datasets.
