import numpy as np
import pandas as pd

# Sample daily temperature data for cities
data = pd.DataFrame({
    "CityA": [70, 72, 68, 71, 73, 69, 75],
    "CityB": [60, 62, 61, 63, 65, 66, 64],
    "CityC": [80, 85, 83, 82, 84, 86, 87]
})

# Calculate mean, standard deviation, and temperature range
mean_temp = data.mean()
std_dev_temp = data.std()
temp_range = data.max() - data.min()

# Identify the most consistent and highest range cities
most_consistent_city = std_dev_temp.idxmin()
highest_range_city = temp_range.idxmax()

print("Yearly Temperature Analysis by City:")
print("  - Mean temperature for each city:")
print(mean_temp)
print("\n  - Standard deviation of temperature for each city:")
print(std_dev_temp)
print(f"\n  - City with the highest temperature range: {highest_range_city} ({temp_range[highest_range_city]}°)")
print(f"  - City with the most consistent temperature: {most_consistent_city} (std dev = {std_dev_temp[most_consistent_city]:.2f})")
