import pandas as pd

# Sample data
data = {
    "CUSTOMER_AGE": [25, 30, 25, 40, 30, 25, 35, 40, 40, 30]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate frequency distribution of ages
age_distribution = df['CUSTOMER_AGE'].value_counts()
print("Frequency Distribution of Customer Ages:\n", age_distribution)
