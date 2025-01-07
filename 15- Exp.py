daily_temperatures = np.array([72, 74, 73, 70, 76, 78, 80, 90, 85, 60, 74, 73, 69, 68])

# Calculate variance
variance = np.var(daily_temperatures)
mean_temp = np.mean(daily_temperatures)
std_dev = np.std(daily_temperatures)

# Define outliers as temperatures more than 3 standard deviations from the mean
outliers = daily_temperatures[np.abs(daily_temperatures - mean_temp) > 3 * std_dev]

print("Daily Temperature Analysis:")
print(f"  - Variance of temperatures: {variance:.2f}")
print(f"  - Potential outliers (unusual temperatures): {outliers if len(outliers) > 0 else 'None detected'}")
