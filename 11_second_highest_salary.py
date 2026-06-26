"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.


Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
"""
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['salary_rank'] = employee['salary'].rank(method='dense', ascending=False)

    result = (
        employee
        .loc[employee['salary_rank'] == 2, ['salary']]
        .drop_duplicates()
    )

    if result.empty:
        return pd.DataFrame({'SecondHighestSalary' : [None]})
    else:
        return result.rename(columns={'salary':'SecondHighestSalary'})