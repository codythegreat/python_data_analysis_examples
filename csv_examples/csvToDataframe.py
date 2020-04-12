# csvExamples.py - opens and reads a csv file's contents
#                  creates a pandas DataFrame from data
#                  and prints cars in order of horsepower

import pandas as pd

# One of the easiest ways to manipulate and print CSV data
# in Python is to use Pandas to parse the file into a 
# DataFrame object
df = pd.read_csv("MOCK_DATA.csv")
print(df)

print("")

# using the read_csv function will create a DataFrame from
# the data in the CSV file. From there we can filter it
print(df.loc[df['make'].isin(['Toyota', 'Suzuki', 'Honda'])])

print("")

# We can also print out the data based on each row's values
# for instance, we can print out the cars based on horsepower
print(df.sort_values(by='horsepower', ascending=False))