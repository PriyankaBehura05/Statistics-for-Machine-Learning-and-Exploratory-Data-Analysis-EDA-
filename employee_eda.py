import pandas as pd

employees = {
"id":[1,2,3,4,5,6,7,8,9,10],
"age":[22,25,28,30,35,40,26,29,32,45],
"salary":[25000,30000,35000,45000,50000,70000,38000,42000,52000,85000],
"experience":[1,2,3,5,7,12,2,4,6,15]
}

df = pd.DataFrame(employees)

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Shape ---")
print(df.shape)

print("\n--- Columns ---")
print(df.columns)

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Statistical Summary ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--Duplicate Records --")
print(df.duplicated().sum())

# Output :
# --- Dataset Info ---
# <class 'pandas.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 4 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   id          10 non-null     int64
#  1   age         10 non-null     int64
#  2   salary      10 non-null     int64
#  3   experience  10 non-null     int64
# dtypes: int64(4)
# memory usage: 452.0 bytes
# None

# --- Shape ---
# (10, 4)

# --- Columns ---
# Index(['id', 'age', 'salary', 'experience'], dtype='str')

# --- Data Types ---
# id            int64
# age           int64
# salary        int64
# experience    int64
# dtype: object

# --- Statistical Summary ---
#              id        age        salary  experience
# count  10.00000  10.000000     10.000000   10.000000
# mean    5.50000  31.200000  47200.000000    5.700000
# std     3.02765   7.067924  18359.375443    4.571652
# min     1.00000  22.000000  25000.000000    1.000000
# 25%     3.25000  26.500000  35750.000000    2.250000
# 50%     5.50000  29.500000  43500.000000    4.500000
# 75%     7.75000  34.250000  51500.000000    6.750000
# max    10.00000  45.000000  85000.000000   15.000000

# --- Missing Values ---
# id            0
# age           0
# salary        0
# experience    0
# dtype: int64

# --- Duplicate Records ---
# 0
# PS D:\Desktop\Statistics for machinelearning and exploring data analysis(EDA)> python -u "d:\Desktop\Statistics for machinelearning and exploring data analysis(EDA)\employee_eda.py"

# --- Dataset Info ---
# <class 'pandas.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 4 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   id          10 non-null     int64
#  1   age         10 non-null     int64
#  2   salary      10 non-null     int64
#  3   experience  10 non-null     int64
# dtypes: int64(4)
# memory usage: 452.0 bytes
# None

# --- Shape ---
# (10, 4)

# --- Columns ---
# Index(['id', 'age', 'salary', 'experience'], dtype='str')

# --- Data Types ---
# id            int64
# age           int64
# salary        int64
# experience    int64
# dtype: object

# --- Statistical Summary ---
#              id        age        salary  experience
# count  10.00000  10.000000     10.000000   10.000000
# mean    5.50000  31.200000  47200.000000    5.700000
# std     3.02765   7.067924  18359.375443    4.571652
# min     1.00000  22.000000  25000.000000    1.000000
# 25%     3.25000  26.500000  35750.000000    2.250000
# 50%     5.50000  29.500000  43500.000000    4.500000
# 75%     7.75000  34.250000  51500.000000    6.750000
# max    10.00000  45.000000  85000.000000   15.000000

# --- Missing Values ---
# id            0
# age           0
# salary        0
# experience    0
# dtype: int64

# --Duplicate Records --
# 0