
"""import matplotlib.pyplot as plt

# Define data
x = ['A', 'B', 'C', 'D']
y = [10, 15, 7, 12]

# Create bar chart
#plt.bar(x, y, label="mild")
plt.bar(x, y)
# Add legend
plt.legend(["mild"])

# Show plot
plt.show()
import math

print("📊 Standard Deviation Calculator for Grouped Data\n")

# Step 1: Get user input for midpoints
midpoints_input = input("Enter the class midpoints (separated by commas): ")
midpoints = [float(x.strip()) for x in midpoints_input.split(",")]

# Step 2: Get user input for frequencies
frequencies_input = input("Enter the frequencies (in same order, separated by commas): ")
frequencies = [int(x.strip()) for x in frequencies_input.split(",")]

# Step 3: Total frequency
total_frequency = sum(frequencies)

# Step 4: Calculate mean
fx = [f * x for f, x in zip(frequencies, midpoints)]
mean = sum(fx) / total_frequency

# Step 5: Squared deviations * frequency
squared_deviation_fx = [(f * (x - mean) ** 2) for f, x in zip(frequencies, midpoints)]

# Step 6: Variance and Standard Deviation
population_variance = sum(squared_deviation_fx) / total_frequency
sample_variance = sum(squared_deviation_fx) / (total_frequency - 1)

population_sd = math.sqrt(population_variance)
sample_sd = math.sqrt(sample_variance)

# Step 7: Output
print("\n📈 Results:")
print("Mean:", round(mean, 2))
print("Population Standard Deviation:", round(population_sd, 2))
print("Sample Standard Deviation:", round(sample_sd, 2))
"""
