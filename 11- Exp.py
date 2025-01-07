import numpy as np

# Sample response times in milliseconds
response_times = np.array([120, 200, 150, 300, 250, 400, 100, 600, 350, 450])

# Calculate percentiles
p25 = np.percentile(response_times, 25)
median = np.percentile(response_times, 50)
p75 = np.percentile(response_times, 75)

print("Server Performance Analysis (Response Times Percentiles):")
print(f"  - 25th percentile of response times: {p25} ms")
print(f"  - 50th percentile (Median) of response times: {median} ms")
print(f"  - 75th percentile of response times: {p75} ms")
