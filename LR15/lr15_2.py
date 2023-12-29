import pandas as pd
import matplotlib.pyplot as plt

# Load the DataFrame from the CSV file for 2011
file_path_2011 = 'Lab15.csv'
bike_path_df_2011 = pd.read_csv(file_path_2011, parse_dates=['Date'], dayfirst=True, sep=',')

# Display the DataFrame for the year 2011
print("******************************************************************")
print("Bike Path Usage Data for 2011:")
print(bike_path_df_2011)

# Group by month and calculate the total number of cyclists
monthly_usage_2011 = bike_path_df_2011.groupby('Month')['Usage'].sum()

# Find the most popular month
most_popular_month_2011 = monthly_usage_2011.idxmax()

# Display the results
print("\nMonthly Usage for 2011:")
print(monthly_usage_2011)

print("\nThe most popular month for cyclists in 2011 is:", most_popular_month_2011)

# Plotting the graph for the year 2011
plt.plot(bike_path_df_2011['Date'], bike_path_df_2011['Usage'], marker='o')
plt.title('Cyclists Visits to Bike Paths in 2011')
plt.xlabel('Date')
plt.ylabel('Number of Cyclists')
plt.show()

# Save the DataFrame to a new CSV file for 2011
bike_path_df_2011.to_csv('Lab15_2011.csv', index=False)
