import pandas as pd

# load the data
data = pd.read_csv('my_data.csv')

# fill in missing values with the mean of the column
data = data.fillna(data.mean())

# save the filled data
data.to_csv('my_filled_data.csv')
