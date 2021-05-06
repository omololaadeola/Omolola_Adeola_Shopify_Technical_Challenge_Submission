# Import library
import os
import csv
from pathlib import Path

# Import Dependencies
import pandas as pd
import numpy as np

# Set path to collect the data
data = os.path.join("C:\\Users\\USER\\Downloads", '2019_Winter_Data_Science_Intern_Challenge_Data_Set.csv')


csv_path = data

# Setting the name and path for file to output
file_to_output = "data_results.txt"

# Import the data set as a DataFrame
data_df = pd.read_csv(csv_path, encoding="utf-8")
data_df.head()

# Identify columns
#data_df.columns

# Identify data info
#data_df.info()

# Question 2: What metric would you report for this dataset?

# Reporting metrics:

# Order Amount (Sum total over the reporting period of the month of March)
# Total Items (Sum total over the reporting period of the month of  March)

# To determine Average Order Value (AOV)

# First determine respective sums of both 'order_amount' and 'total_items'
oa_sum = data_df['order_amount'].sum()
ti_sum = data_df['total_items'].sum()
print(oa_sum)
print(ti_sum)

# Then calculate average by dividing the total order amount (oa_sum) by the total items amount (ti_sum)
AOV = oa_sum/ti_sum
AOV

# Print Average Order Value (AOV) with only 2 decimal places and the dollar sign
print("%.2f" % AOV)

# Print correct explanation with $
'${:,.2f}'.format(AOV)

# Incorrect calculation explained as a mistaken count() instead of sum() function
oa_sum = data_df['order_amount'].sum()
ti_count = data_df['total_items'].count()
AOV = oa_sum/ti_count
print(AOV)



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
