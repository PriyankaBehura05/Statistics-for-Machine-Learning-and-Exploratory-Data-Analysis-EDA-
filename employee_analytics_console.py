import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("HR_Analytics.csv")


def dataset_summary():
    print("\n===== DATASET SUMMARY =====")
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())


def salary_statistics():
    print("\n===== SALARY STATISTICS =====")

    # Change column name if your dataset uses a different salary column
    salary_col = "Salary"

    if salary_col in df.columns:
        print("Mean Salary:", df[salary_col].mean())
        print("Median Salary:", df[salary_col].median())
        print("Maximum Salary:", df[salary_col].max())
        print("Minimum Salary:", df[salary_col].min())
        print("Standard Deviation:", df[salary_col].std())
    else:
        print("Salary column not found in dataset.")


def correlation_analysis():
    print("\n===== CORRELATION ANALYSIS =====")

    corr_matrix = df.corr(numeric_only=True)

    print(corr_matrix)

    corr_matrix.to_csv("correlation_matrix.csv")

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.savefig("correlation_heatmap.png")
    plt.show()

    print("Correlation matrix exported successfully.")


def visualizations():
    print("\n===== VISUALIZATIONS =====")

    numeric_cols = df.select_dtypes(include="number").columns

    # Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df[numeric_cols[0]])
    plt.title(f"{numeric_cols[0]} Distribution")
    plt.savefig("histogram.png")
    plt.show()

    # Box Plot
    plt.figure(figsize=(8, 5))
    plt.boxplot(df[numeric_cols[0]])
    plt.title(f"{numeric_cols[0]} Outliers")
    plt.savefig("boxplot.png")
    plt.show()

    print("Charts saved successfully.")


def export_report():
    with open("report.txt", "w") as file:
        file.write("EMPLOYEE ANALYTICS REPORT\n")
        file.write("=========================\n")
        file.write(f"Dataset Shape: {df.shape}\n")
        file.write(f"Columns: {list(df.columns)}\n")

    print("Report exported as report.txt")


while True:
    print("\n")
    print("===== EMPLOYEE ANALYTICS CONSOLE APP =====")
    print("1. Dataset Summary")
    print("2. Salary Statistics")
    print("3. Correlation Analysis")
    print("4. Visualizations")
    print("5. Export Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        dataset_summary()

    elif choice == "2":
        salary_statistics()

    elif choice == "3":
        correlation_analysis()

    elif choice == "4":
        visualizations()

    elif choice == "5":
        export_report()

    elif choice == "6":
        print("Exiting Application...")
        break

    else:
        print("Invalid Choice! Please try again.")