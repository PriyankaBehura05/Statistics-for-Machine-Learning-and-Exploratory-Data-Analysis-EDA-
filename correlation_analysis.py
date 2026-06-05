import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

employees = {
"age":[22,25,28,30,35,40,26,29,32,45],
"salary":[25000,30000,35000,45000,50000,70000,38000,42000,52000,85000],
"experience":[1,2,3,5,7,12,2,4,6,15]
}

df = pd.DataFrame(employees)

# Correlation
corr_matrix = df.corr()

print(corr_matrix)

# Save CSV
corr_matrix.to_csv("correlation_matrix.csv")

# Visualization
sns.heatmap(corr_matrix, annot=True)
plt.title("Correlation Matrix")

plt.savefig("correlation_heatmap.png")
plt.show()