# DRY - Donot Repeat Yourself
class Emp:
    # emp_id = None
    # name = None
    # salary = None

    # Constructor - used to construct object
    def __init__(self, id, name, salary):
        print("Object Created for",name)
        self.id = id
        self.name = name
        self.salary = salary

    def showDetails(self):
        print(self.name, self.salary)

    def __del__(self):
        print("Object Destructed of",self.name)

emp_1 = Emp(101,"John",45000) # it will __init__ internally

# emp_1.emp_id = 101
# emp_1.name = "John"
# emp_1.salary = 45000
# print(emp_1.name, emp_1.salary)
emp_1.showDetails()

emp_2 = Emp(102,"Shawn",50000)
# emp_2.emp_id = 102
# emp_2.name = "Shawn"
# emp_2.salary = 50000
# print(emp_2.name, emp_2.salary)
emp_2.showDetails()