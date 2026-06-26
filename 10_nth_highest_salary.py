"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.


Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

The result format is in the follow
"""
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee['salary_rank'] = employee['salary'].rank(method='dense', ascending=False)

    result = (
        employee
        .loc[employee['salary_rank'] == N, ['salary']]
        .drop_duplicates()
    )

    if result.empty:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        return result.rename(columns={'salary': f'getNthHighestSalary({N})'})