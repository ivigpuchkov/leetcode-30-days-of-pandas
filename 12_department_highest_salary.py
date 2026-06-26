"""
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.


Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.


Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.
"""
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    result = (
        pd.merge(employee, department, how='inner', left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
        .drop(columns=['departmentId'])
    )
    result['rank_in_dept'] = result.groupby(by='id_dept')['salary'].rank(method='dense', ascending=False)
    return (
        result
        .loc[result['rank_in_dept'] == 1, ['name_dept', 'name_emp', 'salary']]
        .rename(columns={'name_dept':'Department', 'name_emp':'Employee', 'salary':'Salary'})
    )
