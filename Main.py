'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-04 14:55:01
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-04 15:45:19
    @Title : Python OOP Concepts
'''
from Abstraction.Shape import *
from Encapsulation.Bank import *
from Polymorphism.MethodOverloading.Calculator import *
from Polymorphism.MethodOverriding.BackEndDevloper import *
from Polymorphism.MethodOverriding.MLEngineer import *
from Inheritance.Hierarchical import *
from Inheritance.Multilevel import *
from Inheritance.Simple import *
from Inheritance.Multiple import *
from Inheritance.Hybrid import *

if __name__ == "__main__":
    
    print("Abstraction Example")
    radius = int(input("Enter radius : "))
    circle = Circle(radius)
    circle.area()
    length = int(input("Enter length : "))
    square = Square(length)
    square.area()

    print("Encapsulation Example")
    op = Operation()
    op.credit(50000)
    op.withdraw(10000)
    bal = op.get_balance()
    print(f"Your current balance is : {bal}")
    # test = Test()
    # bal = test.get_balance()

    
    print("Polymorphism Example : ")
    
    print("\n1.Method Overloading Example\n")
    calculator = Calculator()
    calculator.add()
    calculator.add(33,99)
    calculator.add(33,99,66)
    
    print("\n2.Method Overriding Example\n")
    ml_eng = MLEngineer("Alice", 24, 105, 9998999899,600000)
    ml_eng.employee_details()
    ml_eng.employee_salary()

    backEndDeveloper = BackEndDeveloper("John", 25, 101, 9789878978,400000)
    backEndDeveloper.employee_details()
    backEndDeveloper.employee_salary()


    print("Inheritance Example : ")
    
    print("\n1.Simple Inheritance\n")
    son = Son()
    son.books()
    son.games()
    son.father_property()
    son.property()

    print("\nHierarchical Inheritance Example\n")
    mathsTeacher = MathsTeacher("Kyara", 25, 9797979797, "Saint Marry Public school")
    mathsTeacher.teacher_details()
    mathsTeacher.subject()
    print()
    scienceTeacher = ScienceTeacher("Myra", 25, 9989989595, "Delhi Public school")
    scienceTeacher.teacher_details()
    scienceTeacher.subject()

    print("\nMultilevel Inheritance Example\n")
    samsungS10Lite = SamsungS10Lite()
    samsungS10Lite.brand()
    samsungS10Lite.model()
    samsungS10Lite.os()
    samsungS10Lite.mobile_features()
    samsungS10Lite.specifications()

    print("\nMultiple Inheritance")
    john = TeamLeader()
    john.set_title("Team Lead")
    john.set_pay(900000)
    john.set_project("Python Zen")
    john.set_exp(6)
    john.details()

    print("\nHybrid Inheritance\n")
    s_car = SportsCar()
    s_car.vehicle_info()
    s_car.car_info()
    s_car.sports_car_info()    