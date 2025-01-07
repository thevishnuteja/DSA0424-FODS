import pandas as pd

# Sample data
data = {
    "LIKES": [100, 150, 100, 200, 150, 100, 300, 200, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate frequency distribution of likes
like_distribution = df['LIKES'].value_counts()
print("Frequency Distribution of Likes:\n", like_distribution)
