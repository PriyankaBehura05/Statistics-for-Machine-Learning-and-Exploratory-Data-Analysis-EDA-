# Analysis Report: Statistics and Exploratory Data Analysis (EDA)

## 1. Why is data cleaning important before ML training?

Data cleaning is an essential step before training any machine learning model because real-world datasets often contain missing values, duplicate records, incorrect entries, and inconsistent formatting. Machine learning algorithms learn patterns directly from the data they receive. If the input data contains errors, the model will learn incorrect patterns and produce inaccurate results.

Data cleaning improves data quality by removing duplicates, handling missing values, correcting inconsistencies, and ensuring that all features are properly formatted. Clean data helps models train faster, improves prediction accuracy, and reduces bias. It also makes the dataset more reliable and easier to analyze during the EDA process.

For example, if an employee salary dataset contains missing salary values or duplicate employee records, the calculated statistics such as mean and median may become inaccurate. Cleaning the dataset ensures that the analysis and machine learning model are based on reliable information.

---

## 2. What happens if outliers are ignored?

Outliers are data points that are significantly different from the rest of the dataset. They may occur because of data entry errors, measurement errors, or genuine unusual observations. Ignoring outliers can negatively affect statistical analysis and machine learning models.

Outliers can distort the mean, variance, and standard deviation of a dataset. They may also influence the decision boundaries of machine learning algorithms, causing poor predictions. For example, if most employee salaries range between ₹30,000 and ₹80,000 but one salary is recorded as ₹10,00,000, the average salary will increase significantly and no longer represent the majority of employees.

However, not all outliers should be removed. Some outliers may represent important business information. Therefore, data analysts must first investigate the cause of the outlier before deciding whether to remove or retain it.

---

## 3. Why do we calculate correlation?

Correlation is calculated to measure the relationship between two variables. It helps us understand whether one variable increases or decreases when another variable changes. Correlation values range from -1 to +1.

A positive correlation indicates that both variables move in the same direction, while a negative correlation indicates that they move in opposite directions. A value close to zero suggests little or no relationship.

Correlation analysis is important because it helps identify meaningful relationships in data. For example, in an employee dataset, experience and salary often have a positive correlation because employees with more experience generally earn higher salaries. Understanding these relationships helps data scientists select important features and improve machine learning model performance.

Correlation matrices and heatmaps are commonly used during EDA to visualize relationships among multiple variables.

---

## 4. Why is EDA important before building a chatbot knowledge base?

EDA is important before building a chatbot knowledge base because it helps evaluate the quality, completeness, and structure of the data that will be used by the chatbot. A chatbot relies on accurate and relevant information to answer user queries correctly.

Through EDA, engineers can identify missing information, duplicate records, irrelevant content, and inconsistencies in the dataset. It also helps understand the distribution and organization of data before it is indexed into a knowledge base.

For example, if a customer support chatbot is trained using duplicated FAQ documents or outdated information, users may receive incorrect responses. EDA helps detect such issues early and ensures that the chatbot knowledge base contains clean, accurate, and well-structured information.

A properly analyzed knowledge base improves response quality, user satisfaction, and overall chatbot performance.

---

## 5. How can poor data affect an LLM or RAG system?

Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) systems depend heavily on the quality of the data used for training and retrieval. Poor-quality data can introduce inaccuracies, bias, misinformation, and inconsistencies into the system.

If an LLM is trained on noisy or incorrect data, it may generate misleading or factually incorrect responses. Similarly, a RAG system retrieves information from a knowledge base before generating an answer. If the retrieved documents contain outdated, duplicated, or inaccurate information, the generated response may be unreliable.

Poor data can also increase hallucinations, where the model produces information that appears correct but is actually false. In business applications, this can reduce user trust and lead to poor decision-making.

Therefore, data cleaning, validation, EDA, and continuous monitoring are essential to ensure that LLMs and RAG systems provide accurate, trustworthy, and useful responses.

---
