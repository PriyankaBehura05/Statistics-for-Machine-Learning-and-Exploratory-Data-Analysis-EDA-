import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("HR_Analytics.csv")

# Dataset Information
print("First 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
df.info()

# Missing Values Check
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Records Check
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Correlation Analysis
corr_matrix = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(corr_matrix)

# Save Correlation Matrix
corr_matrix.to_csv("correlation_matrix.csv")

# Correlation Heatmap
plt.figure(figsize=(20, 18))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix")
plt.tight_layout()

plt.savefig("correlation_heatmap.png", dpi=300)
plt.show()

print("\nFiles Generated Successfully:")
print("1. correlation_matrix.csv")
print("2. correlation_heatmap.png")