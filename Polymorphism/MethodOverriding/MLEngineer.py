from Polymorphism.MethodOverriding.Employee import Employee
class MLEngineer(Employee):
    def __init__(self,name ,age,id,mobile_number,salary):
        self.salary = salary
        Employee.__init__(self,name,age,id,mobile_number)
    def employee_salary(self):
        print(f"ML Engineer Salary  : {self.salary}")