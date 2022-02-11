employees_1 = {
    "names" : ["John","Mac","Tom","Nick","Sam","Shawn"],
    "dept" : ["IT","HR","IT","IT","HR","HR"],
    "salary" : [45000, 50000, 35000,67000,55000,80000]
    }

#1. Take Employee name as input and print his dept and salary without using loop

emp_name = input("Enter employee name : ")
index = employees_1["names"].index(emp_name)
print(employees_1["dept"][index], employees_1["salary"][index])

#2. Find out average salary of IT department employees
