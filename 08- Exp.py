import numpy as np

# Sample quarterly sales data
sales_data = np.array([150000, 160000, 175000, 200000])

# Calculate total sales for the year
total_sales = sales_data.sum()

# Calculate percentage increase from Q1 to Q4
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print(f"Total sales for the year: ${total_sales:,.2f}")
print(f"Percentage increase from Q1 to Q4: {percentage_increase:.2f}%")
