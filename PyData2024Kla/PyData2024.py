import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('c:/Users/user/Desktop/Data Visualization using Matplotlib/Data-Visualization-in-Matplotlib/PyData2024Kla/loanData.csv')

# Step 2: Bar plot for the count of loans by Property_Area
plt.figure(figsize=(10, 6))
df['Property_Area'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Count of Loans by Property Area')
plt.xlabel('Property Area')
plt.ylabel('Count of Loans')
plt.show()

# Step 3: Pie chart for the distribution of Loan_Status
plt.figure(figsize=(8, 8))
df['Loan_Status'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'lightcoral'])
plt.title('Distribution of Loan Status')
plt.ylabel('')
plt.show()

# Step 4: Histogram for the distribution of LoanAmount
plt.figure(figsize=(10, 6))
df['LoanAmount'].fillna(df['LoanAmount'].median()).plot(kind='hist', bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Loan Amount')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.show()

# Step 5: Scatter plot for ApplicantIncome vs LoanAmount
plt.figure(figsize=(10, 6))
plt.scatter(df['ApplicantIncome'], df['LoanAmount'], alpha=0.5, color='blue')
plt.title('Applicant Income vs Loan Amount')
plt.xlabel('Applicant Income')
plt.ylabel('Loan Amount')
plt.show()