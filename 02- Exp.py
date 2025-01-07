import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Sample data
data = {
    'SmokingRate': [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
    'LungCancerRate': [30, 35, 40, 55, 60, 70, 80, 90, 100, 120]
}

df = pd.DataFrame(data)
correlation = df['SmokingRate'].corr(df['LungCancerRate'])
print("Correlation Coefficient between SmokingRate and LungCancerRate:", correlation)

plt.scatter(df['SmokingRate'], df['LungCancerRate'], color='blue')
plt.title("Smoking Rate vs Lung Cancer Rate")
plt.xlabel("Smoking Rate (%)")
plt.ylabel("Lung Cancer Rate (per 100,000)")
plt.grid(True)
plt.show()
