import pandas as pd

# Sample employee data
data = {
    'Employee_ID': [1, 2, 3, 4, 5, 6, 7],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Salary': [60000, 70000, 65000, 68000, 72000, 64000, 67000],
    'Joining_Date': pd.to_datetime(['2020-01-15', '2019-05-20', '2018-07-10', '2021-02-17', '2017-08-30', '2022-01-01', '2019-11-11'])
}
employee_data = pd.DataFrame(data)

# Highest and lowest salaries in each department
print("Highest and lowest salaries in each department:\n", employee_data.groupby('Department')['Salary'].agg(['max', 'min']))

# Average tenure of employees
employee_data['Tenure'] = (pd.to_datetime("today") - employee_data['Joining_Date']).dt.days / 365
print(f"\nAverage tenure of employees: {employee_data['Tenure'].mean():.2f} years")

# Employees who joined before 2020-01-01
print("\nEmployees who joined before 2020-01-01:")
print(employee_data[employee_data['Joining_Date'] < '2020-01-01'][['Employee_ID', 'Joining_Date']].to_string(index=False))
