import numpy as np

# Sample data: prices for 3 products over a period
sales_data = np.array([
    [120.5, 130.75, 110.25],
    [90.75, 88.25, 100.50],
    [115.5, 120.0, 105.75]
])

# Find the average price across all products
average_price = sales_data.mean()

print(f"Average price of all products sold: {average_price:.2f}")
