'''import pandas as pd
df = pd.read_csv("dataset.csv")
print(df)
'''
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
mpce_data = np.random.normal(loc=10000, scale=3000, size=1000)  # Mean = 10000, Std Dev = 3000


mpce_data = np.abs(mpce_data)


plt.figure(figsize=(10, 5))
plt.hist(mpce_data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(np.mean(mpce_data), color='red', linestyle='dashed', linewidth=2, label="Mean MPCE")
plt.xlabel("MPCE (Monthly Per Capita Expenditure)")
plt.ylabel("Frequency")
plt.title("Histogram of MPCE Distribution")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)


plt.show()



