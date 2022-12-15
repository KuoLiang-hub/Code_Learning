import pandas as pd

# load the first table into a DataFrame
df1 = pd.read_csv("table1.csv")

# load the second table into a DataFrame
df2 = pd.read_csv("table2.csv")

# join the two tables on the "key" column
result = pd.merge(df1, df2, on="key")

# display the resulting DataFrame
print(result)
