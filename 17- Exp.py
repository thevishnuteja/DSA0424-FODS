# Sample daily sales data
daily_sales = np.array([120, 150, 130, 170, 160, 150, 145, 155, 140, 165])

# Calculate variance of daily sales
sales_variance = np.var(daily_sales)

print("Sales Variance Analysis:")
print(f"  - Variance of daily sales: {sales_variance:.2f}")
print("  - Interpretation: A higher variance indicates larger fluctuations in daily sales, while a lower variance suggests more consistent sales.")
