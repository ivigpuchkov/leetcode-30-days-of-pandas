"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.


Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in any order.
"""
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return(
        teacher.groupby('teacher_id')['subject_id']
        .nunique()
        .reset_index()
        .rename(columns={'subject_id':'cnt'})
        .loc[:, ['teacher_id', 'cnt']]
    )