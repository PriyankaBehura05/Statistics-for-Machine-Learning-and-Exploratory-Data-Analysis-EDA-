from collections import Counter
import math

# Dataset
scores = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# 1. Mean
mean = sum(scores) / len(scores)


# 3. Mode
frequency = Counter(scores)
mode = frequency.most_common(1)[0][0]

# 4. Variance
variance = sum((x - mean) ** 2 for x in scores) / len(scores)

# 5. Standard Deviation
std_deviation = math.sqrt(variance)

# Output
print("Dataset:", scores)
print("\n--- Statistics Results ---")
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)

#output :
# Dataset: [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# --- Statistics Results ---
# Mean: 67.5
# Median: 67.5
# Mode: 45
# Variance: 206.25
# Standard Deviation: 14.361406616345072