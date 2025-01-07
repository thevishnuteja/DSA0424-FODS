import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Category': ['Electronics', 'Clothing', 'Home & Kitchen', 'Beauty', 'Sports', 'Toys', 'Books', 'Automotive'],
    'TotalSales': [50000, 30000, 45000, 15000, 25000, 20000, 10000, 18000]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['TotalSales'], color='skyblue')
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Category'], df['TotalSales'], color='purple')
plt.title("Sales Distribution across Product Categories")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Category'], df['TotalSales'], marker='o', color='green')
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
