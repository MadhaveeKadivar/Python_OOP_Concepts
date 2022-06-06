class Employee:
    def __init__(self,name ,age,id,mobile_number):
        self.name = name
        self.age = age
        self.id = id
        self.mobile_number = mobile_number
        
    def employee_details(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee Age : {self.age}")
        print(f"Employee Id : {self.id}")
        print(f"Employee Moile Number : {self.mobile_number}")
    
    def employee_salary(self):
        pass
        