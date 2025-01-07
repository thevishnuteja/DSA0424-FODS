import numpy as np

# Sample data: fuel efficiency of different car models
fuel_efficiency = np.array([25.5, 30.2, 27.8, 32.0, 29.5])

# Calculate the average fuel efficiency
average_fuel_efficiency = fuel_efficiency.mean()

# Calculate percentage improvement between two specific car models (e.g., model 1 and model 4)
percentage_improvement = ((fuel_efficiency[3] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

print(f"Average fuel efficiency: {average_fuel_efficiency:.2f} mpg")
print(f"Percentage improvement between model 1 and model 4: {percentage_improvement:.2f}%")
