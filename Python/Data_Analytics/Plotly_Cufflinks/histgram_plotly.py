import plotly.express as px

# Create a list of data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Use the histogram function from the plotly.express module to create a histogram figure
# Specify the color of the bars as red
fig = px.histogram(data, x='data', title='Histogram', color='red')

# Display the figure
fig.show()

# You can also use the barmode argument to specify the style of the bars. 
# Valid options are 'overlay', 'stack', and 'relative':
fig = px.histogram(data, x='data', title='Histogram', barmode='stack')

# Display the figure
fig.show()
