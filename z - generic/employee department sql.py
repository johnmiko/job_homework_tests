"""
employee table
id
name
manager_id -- is the id of the employee
department id

department table
id
name

1) query, list employee name with department name

SELECT employee.name, department.name FROM employee_table
join department_table on department_table.id = employee_table.department_id

import pandas as pd
fname_employee = 'employees.csv'
fname_department = 'departments.csv'
df_employee = pd.read_csv(fname_employee)
df_department = pd.read_csv(fname_department)
df = pd.merge(df_employee, df_department, left_on='department_id', right_on='id')
print(df[['name', 'name_x']].to_string())




2) We deleted a couple departments, forgot to delete the ids from the employee table
    Give list of employee who have stale departments

select employee.id, employee.name from employee_table
left join department_table on department_table.id = employee_table.department_id
where isnull(department.name)

df = pd.merge(df_employee, df_department, left_on='department_id', right_on='id', how='left')
df2 = df[df['department_name'].isna()]
df2
print(df2[['name']].to_string())


3) Manager id in employee table
    IS employee id or id of manager
    List all employee names with manager names

df['manager_name'] = df.loc[df['employee_id'] = df['manager_id'], 'employee_name']
print(df2[['employee_name','manager_name']].to_string())

-- can use a self join - read about
select name, manager_name from employee_table
manager_name = (select name from employee_table WHERE employee_id = manager_id)




"""
