import numpy as np
from scipy import stats

# Sample purchase amounts in dollars
purchase_amounts = np.array([20, 35, 45, 20, 60, 20, 45, 60, 20, 70])

# Calculate mean and mode
mean_purchase = np.mean(purchase_amounts)
mode_purchase = stats.mode(purchase_amounts, keepdims=True).mode

print("E-commerce Purchase Amount Analysis:",
      f"Mean: ${mean_purchase:.2f},",
      f"Mode: ${mode_purchase[0] if mode_purchase.size > 0 else 'No mode found'}")
