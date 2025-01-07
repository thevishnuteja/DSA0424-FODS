import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [2000, 2500, 3000, 2800, 3200, 3600, 4000, 3800, 3700, 3500, 3300, 3400]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', color='blue', linestyle='-')
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='orange')
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.show()
