from abc import ABC, abstractmethod
class Shape(ABC): # Inheriting abstract class
    @abstractmethod
    def area(self):
        """ 
        Description: 
            This function is doing nothing
        Parameter:
            It takes one self as argument
        Return:
            None
        """
        pass
 
class Circle(Shape):
    def __init__(self,radius):
        """ 
        Description: 
            Constuctor
        Parameter:
            It takes self and radius as argument
        Return:
            None
        """
        self.radius = radius
    def area(self):
        """ 
        Description: 
            This function is calculating area of circle
        Parameter:
            It takes one self as argument
        Return:
            None
        """
        a = 3.14 * self.radius * self.radius
        print(f"Area of Circle is : {a}")

class Square(Shape):
    def __init__(self,length):
        """ 
        Description: 
            Constuctor
        Parameter:
            It takes self and length as argument
        Return:
            None
        """
        self.length = length

    def area(self):
        """ 
        Description: 
            This function is calculating area of square
        Parameter:
            It takes one self as argument
        Return:
            None
        """
        a = self.length * self.length
        print(f"Area of Square is : {a}")