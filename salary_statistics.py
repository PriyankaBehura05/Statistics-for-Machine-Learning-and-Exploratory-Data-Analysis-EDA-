import math

salaries = [
25000, 30000, 35000, 40000, 45000,
50000, 55000, 60000, 65000, 70000
]


# Mean

total = 0
for sal in salaries:
    total += sal

mean = total / len(salaries)


# Median

salaries.sort()
n = len(salaries)

if n % 2 == 0:
    median = (salaries[n//2 - 1] + salaries[n//2]) / 2
else:
    median = salaries[n//2]


# Variance

variance_sum = 0

for sal in salaries:
    variance_sum += (sal - mean) ** 2

variance = variance_sum / len(salaries)


# Standard Deviation

std_dev = math.sqrt(variance)


# Highest & Lowest

highest = max(salaries)
lowest = min(salaries)


print("Salary Statistics Report : ")
print("----------------------------")
print("Mean Salary:", mean)
print("Median Salary:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Highest Salary:", highest)
print("Lowest Salary:", lowest)


#output : 

# Salary Statistics Report :

# Mean Salary: 47500.0
# Median Salary: 47500.0
# Variance: 206250000.0
# Standard Deviation: 14361.406616345072
# Highest Salary: 70000
# Lowest Salary: 25000