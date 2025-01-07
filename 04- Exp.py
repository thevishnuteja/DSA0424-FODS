import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [5, 7, 12, 16, 20, 25, 30, 28, 24, 18, 12, 7],
    'Rainfall': [78, 60, 50, 42, 60, 80, 120, 110, 90, 85, 70, 75]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Temperature'], marker='o', color='orange', label="Temperature (°C)")
plt.plot(df['Month'], df['Rainfall'], marker='o', color='blue', label="Rainfall (mm)")

plt.title("Monthly Temperature and Rainfall")
plt.xlabel("Month")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Month'], df['Temperature'], color='red')
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Month'], df['Rainfall'], color='blue')
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['Temperature'], df['Rainfall'], color='purple')
plt.title("Temperature vs. Rainfall")
plt.xlabel("Temperature (°C)")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()
