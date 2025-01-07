import pandas as pd

data = {
    'OrderID': [1, 1, 2, 2, 3, 3, 4, 4, 5],
    'CustomerID': [101, 101, 102, 102, 103, 103, 104, 104, 105],
    'ProductID': ['A1', 'A2', 'A1', 'A3', 'A2', 'A3', 'A1', 'A4', 'A2'],
    'Quantity': [2, 1, 3, 2, 5, 1, 4, 2, 1],
    'TotalPrice': [200, 100, 300, 150, 500, 100, 400, 200, 100]
}

df = pd.DataFrame(data)

print(df)


print(df.info())

print(df.isnull().sum())
print(df.describe())
total_sales = df['TotalPrice'].sum()
print("Total Sales: ", total_sales)

total_quantity = df['Quantity'].sum()
print("Total Quantity of Products Sold: ", total_quantity)
average_order_value = df['TotalPrice'].sum() / df['OrderID'].nunique()
print("Average Order Value: ", average_order_value)
top_products = df.groupby('ProductID')['Quantity'].sum().sort_values(ascending=False)
print("Top Products by Quantity Sold:")
print(top_products.head())
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False)
print("Top Customers by Total Spending:")
print(top_customers.head())
average_quantity_per_order = df['Quantity'].sum() / df['OrderID'].nunique()
print("Average Quantity per Order: ", average_quantity_per_order)
