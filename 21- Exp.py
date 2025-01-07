import pandas as pd

# Sample data
data = {
    "WEATHER_CONDITION": ["Sunny", "Rainy", "Cloudy", "Snowy", "Windy"],
    "OCCURRENCES": [180, 150, 130, 20, 30]
}

# Create DataFrame
df = pd.DataFrame(data)

# Find the most common weather condition
most_common_weather = df.loc[df['OCCURRENCES'].idxmax()]
print("Most Common Weather Condition:", most_common_weather['WEATHER_CONDITION'])
print("Occurrences:", most_common_weather['OCCURRENCES'])
