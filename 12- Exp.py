# Sample recovery times in days
recovery_times = np.array([5, 10, 7, 14, 8, 6, 9, 12, 11, 15, 8, 13, 7])

# Calculate percentiles
p10 = np.percentile(recovery_times, 10)
median = np.percentile(recovery_times, 50)
p90 = np.percentile(recovery_times, 90)

print("Medical Study - Recovery Times Distribution:")
print(f"  - 10th percentile (Fast recoveries): {p10} days")
print(f"  - 50th percentile (Median recovery time): {median} days")
print(f"  - 90th percentile (Slow recoveries): {p90} days")
