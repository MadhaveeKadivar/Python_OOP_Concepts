class Teacher:
    def __init__(self,name,age,mobile_number,school_name):
        """ 
        Description: 
            Constructor
        Parameter:
            It takes name,age,mobile number and school name as argument
        Return:
            None
        """
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.school_name = school_name
            
    def teacher_details(self):
        """ 
        Description: 
            This function is used for printing teacher details
        Parameter:
            It takes self as argument
        Return:
            None
        """
        print(f"Teacher's Name : {self.name}")
        print(f"Teacher's Age : {self.age}")
        print(f"Teacher's Moile Number : {self.mobile_number}")
        print(f"Teacher's School Name: {self.school_name}")

class ScienceTeacher(Teacher):
    def __init__(self,name,age,mobile_number,school_name):
        """ 
        Description: 
            Constructor
        Parameter:
            It takes name,age,mobile number and school name as argument
        Return:
            None
        """
        Teacher.__init__(self,name,age,mobile_number,school_name)
    def subject(self):
        """ 
        Description: 
            Printing subject of science teacher
        Parameter:
            It takes self as argument
        Return:
            None
        """
        print(f"{self.name} teaching Science subject")

class MathsTeacher(Teacher):
    def __init__(self,name,age,mobile_number,school_name):
        """ 
        Description: 
            Constructor
        Parameter:
            It takes name,age,mobile number and school name as argument
        Return:
            None
        """
        Teacher.__init__(self,name,age,mobile_number,school_name)
    def subject(self):
        """ 
        Description: 
            Printing subject of Maths teacher
        Parameter:
            It takes self as argument
        Return:
            None
        """
        print(f"{self.name} teaching Maths subject")