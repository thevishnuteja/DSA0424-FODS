import pandas as pd
from scipy.stats import norm

# Sample data
data = {
    "product_title": ["Pineapple slicer", "Levis Jeans Pant", "Wallet", "Salwar"],
    "product_category": ["Apparel", "Apparel", "Apparel", "Apparel"],
    "star_rating": [4, 5, 5, 5],
    "review_headline": ["Really good", "Perfect Dress", "Love it", "Awesome"],
    "review_date": ["2013-01-14", "2014-04-22", "2015-07-28", "2015-06-12"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Filter for "Apparel" category
apparel_ratings = df[df['product_category'] == 'Apparel']['star_rating']

# Calculate mean rating
mean_rating = apparel_ratings.mean()

# Calculate standard deviation and sample size
std_dev = apparel_ratings.std()
n = len(apparel_ratings)

# Calculate 95% confidence interval
z = norm.ppf(0.975)  # Z-score for 95% confidence
margin_of_error = z * (std_dev / n**0.5)
confidence_interval = (mean_rating - margin_of_error, mean_rating + margin_of_error)

print("Mean Rating:", mean_rating)
print("95% Confidence Interval:", confidence_interval)
