"""
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.


Write a solution to find managers with at least five direct reports.

Return the result table in any order.
"""
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = (
        employee.groupby('managerId')
        .agg(reports = ('id', 'count'))
        .reset_index()
    )
    valid_managers_ids = managers.loc[managers['reports'] >=5, 'managerId']
    return (
        employee.loc[employee['id'].isin(valid_managers_ids), ['name']]
    )