import numpy as np

# Sample monthly expenses for each department (rows are departments, columns are months)
expenses = np.array([
    [2000, 2500, 3000, 2200],
    [1500, 1800, 2000, 2100],
    [3000, 3200, 3100, 3300]
])

# Calculate variance and covariance matrix
variance = np.var(expenses, axis=1)
covariance_matrix = np.cov(expenses, rowvar=True)

print("Monthly Expenses Analysis for Departments:")
for i, var in enumerate(variance):
    print(f"  - Department {i+1} variance in expenses: {var:.2f}")
print("\nCovariance matrix of expenses between departments:")
print(covariance_matrix)
