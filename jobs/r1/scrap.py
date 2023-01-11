"""
2 threads
1 to print even numbers, other to print odd numbers

1,2,3,4,
import threading
t1 = new thread();
t2 = new thread();
t1 = [0,2,4,6,8...];
t2 = [1,3,5,7...];
await t1[0]
await t2[0]

class Tree
    Node left
    Node right

tree = new Tree();
tree.left;
tree.right;

List of students
Convert into map of student id, and student (id, name)
map = new dict();
for student in students:
    map[student.id] = student

Performance issue SQL
    denormalize
    index

simple query to Employee, Department tables
    Employee
        Id
        name
        department id
        salary

    Department
        department id
        department name
    output name of employee who has the highest salary in his department and department name
    select e.name, department.name  from employee as e
        left join department on department.id = employee.department_id
        group by e.department_id
        max(salary)


"""
