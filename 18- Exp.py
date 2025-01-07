import pandas as pd
import matplotlib.pyplot as plt

# Sample data in a DataFrame
data = {
    'Month': ['January', 'February', 'March'],
    'Sales Units': [150, 130, 170],
    'Revenue': [120000, 104000, 136000]
}
df = pd.DataFrame(data).set_index('Month')

# Plotting Sales Units and Revenue
df.plot(subplots=True, layout=(1, 2), figsize=(10, 5), marker='o', grid=True, title=["Sales (Units)", "Revenue ($)"])
plt.tight_layout()
plt.show()
