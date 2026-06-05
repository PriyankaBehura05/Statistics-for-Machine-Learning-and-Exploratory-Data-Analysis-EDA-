# Statistics & Exploratory Data Analysis (EDA)

## Project Overview

This project focuses on understanding the fundamental concepts of **Statistics** and **Exploratory Data Analysis (EDA)**, which are essential for building Machine Learning, Deep Learning, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) systems, Recommendation Engines, and AI Analytics solutions.

The objective is to analyze datasets, understand data distributions, identify patterns, detect outliers, perform correlation analysis, and generate meaningful visualizations before training machine learning models.

---

#  Learning Objectives

- Understand statistical concepts used in Machine Learning.
- Calculate measures of central tendency and variability.
- Perform Exploratory Data Analysis (EDA).
- Analyze relationships between features using correlation.
- Visualize data using charts and plots.
- Work with real-world datasets.
- Generate insights from data for decision-making.

---

# Project Structure

```text
day3-statistics-eda/
│
├── statistics_basics.py
├── salary_statistics.py
├── employee_eda.py
├── correlation_analysis.py
├── visualizations.py
├── real_dataset_analysis.py
├── employee_analytics_console.py
├── analysis_report.md
├── README.md
│
├── charts/
│   ├── salary_distribution.png
│   ├── correlation_heatmap.png
│   ├── salary_boxplot.png
│   ├── experience_salary_scatter.png
│   └── age_salary_linechart.png
│
├── reports/
│   ├── correlation_matrix.csv
│   └── insights_report.md
│
└── dataset/
    └── HR_Analytics.csv
```

---

#  Task 1: Statistics Fundamentals

### Dataset

```python
scores = [45,50,55,60,65,70,75,80,85,90]
```

### Calculated Metrics

- Mean
- Median
- Mode
- Variance
- Standard Deviation

### Concepts Covered

- Central Tendency
- Data Spread
- Statistical Analysis

---

# Task 2: Salary Statistics

### Dataset

Employee salary records were analyzed to calculate:

- Mean Salary
- Median Salary
- Variance
- Standard Deviation
- Highest Salary
- Lowest Salary

### Objective

To understand salary distribution and variability within an organization.

---

# Task 3: Salary Distribution Analysis

Generated 100 random employee salaries using NumPy and performed:

- Distribution Analysis
- Mean Comparison
- Outlier Detection
- Histogram Visualization

### Output

```text
salary_distribution.png
```

---

#  Task 4: Employee Exploratory Data Analysis (EDA)

Performed analysis on employee data including:

### Dataset Information

- Shape
- Columns
- Data Types

### Data Quality Checks

- Missing Values
- Duplicate Records

### Statistical Summary

```python
df.describe()
```

### Objective

To understand the structure and quality of the dataset before applying Machine Learning.

---

#  Task 5: Correlation Analysis

Analyzed relationships between:

- Age vs Salary
- Experience vs Salary
- Age vs Experience

### Output Files

```text
correlation_matrix.csv
correlation_heatmap.png
```

### Objective

To identify feature relationships and dependencies.

---

# Task 6: Data Visualization

Created multiple visualizations for data analysis.

### Visualizations Generated

#### Histogram
- Salary Distribution

#### Scatter Plot
- Experience vs Salary

#### Box Plot
- Salary Outlier Detection

#### Line Chart
- Age vs Salary

### Output

```text
salary_distribution.png
experience_salary_scatter.png
salary_boxplot.png
age_salary_linechart.png
```

---

# Task 7: Real Dataset Analysis

A real HR Analytics dataset was downloaded and analyzed.

### Activities Performed

#### Data Cleaning

- Missing Value Detection
- Duplicate Record Detection
- Data Validation

#### Statistical Summary

- Mean
- Median
- Standard Deviation
- Min/Max Values

#### Correlation Analysis

- Feature Relationship Analysis
- Correlation Matrix Generation

#### Visualization

- Heatmaps
- Histograms
- Box Plots
- Scatter Plots

#### Insights Report

Generated business insights based on dataset observations.

---

# Task 8: AI Engineer Thinking Exercise

Created:

```text
analysis_report.md
```

### Topics Covered

- Importance of Data Cleaning
- Impact of Outliers
- Correlation Analysis
- Importance of EDA
- Data Quality in LLM and RAG Systems

---

#  Bonus Challenge

## Employee Analytics Console Application

Developed a menu-driven console application with the following features:

```text
1. Dataset Summary
2. Salary Statistics
3. Correlation Analysis
4. Visualizations
5. Export Report
6. Exit
```

### Benefits

- Interactive Data Analysis
- Automated Reporting
- Visualization Generation

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

#  Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd day3-statistics-eda
```

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

---

# Running the Project

Run individual tasks:

```bash
python statistics_basics.py
python salary_statistics.py
python employee_eda.py
python correlation_analysis.py
python visualizations.py
python real_dataset_analysis.py
```

Run the Bonus Console Application:

```bash
python employee_analytics_console.py
```

---

# Key Learnings

Through this project, I learned:

- Statistical analysis fundamentals
- Exploratory Data Analysis (EDA)
- Data cleaning techniques
- Correlation analysis
- Data visualization
- Real-world dataset handling
- Data preparation for Machine Learning and AI systems

---


##  Author

**Priyanka Behura**

Aspiring AI/ML Engineer passionate about Data Science, Machine Learning, Deep Learning, Generative AI, and Large Language Models.
