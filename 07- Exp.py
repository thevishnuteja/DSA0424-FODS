import numpy as np

# Sample house data with columns [bedrooms, square footage, sale price]
house_data = np.array([
    [3, 1500, 350000],
    [5, 2500, 500000],
    [4, 1800, 400000],
    [6, 3000, 600000],
    [5, 2700, 550000]
])

# Filter rows where bedrooms > 4
houses_with_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]

# Calculate the average sale price of these houses
average_price = houses_with_more_than_4_bedrooms[:, 2].mean()

print(f"Average sale price for houses with more than four bedrooms: ${average_price:,.2f}")
