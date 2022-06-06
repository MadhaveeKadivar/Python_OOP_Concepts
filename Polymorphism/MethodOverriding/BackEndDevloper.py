from Polymorphism.MethodOverriding.Employee import Employee
class BackEndDeveloper(Employee):
    def __init__(self,name ,age,id,mobile_number,salary):
        self.salary = salary
        Employee.__init__(self,name,age,id,mobile_number)
    def employee_salary(self):
        print(f"Back End Developer Salary  : {self.salary}")