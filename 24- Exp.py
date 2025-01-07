import pandas as pd
from collections import Counter

# Sample data
data = {
    "REVIEW": ["Great product", "Very good product", "Good quality product", "Really great and good"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Tokenize and count word frequencies
all_words = " ".join(df['REVIEW']).lower().split()
word_distribution = Counter(all_words)

print("Frequency Distribution of Words in Reviews:\n", word_distribution)
