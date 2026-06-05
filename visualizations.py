import pandas as pd
import matplotlib.pyplot as plt

# Dataset
employees = {
"age":[22,25,28,30,35,40,26,29,32,45],
"salary":[25000,30000,35000,45000,50000,70000,38000,42000,52000,85000],
"experience":[1,2,3,5,7,12,2,4,6,15]
}

df = pd.DataFrame(employees)


# Histogram - Salary Distribution
plt.hist(df["salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.savefig("salary_histogram.png")
plt.close()


# Scatter Plot - Experience vs Salary

plt.scatter(df["experience"], df["salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.savefig("experience_salary_scatter.png")
plt.close()


# Box Plot - Salary Outliers

plt.boxplot(df["salary"])
plt.title("Salary Outliers")
plt.savefig("salary_boxplot.png")
plt.close()


# Line Chart - Age vs Salary

plt.plot(df["age"], df["salary"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.savefig("age_salary_linechart.png")
plt.close()

print("All charts saved successfully!")