 # types of method
 # instance method -> works with instant variablr
 # class method -> works with class variable
 # static method
 
 # instance method has two types 
 # 1. accessor(only get instant variable) 
 # 2.mutator (to change instant variable)
 
 # class method works with class variable
 
 # static method has nothing to do with class or instance variable
 
class Student:
    school="Telusko"
    def __init__(self,m1,m2,m3) -> None:
        self.m1=m1
        self.m2=m2
        self.m3=m3
     
    def avg(self): # its an instance as it works with object
        return (self.m1+self.m2+self.m3)/3
    
    def get_m1(self): # this method is called accessor method as it is just used
        # to fetch instance variable
        return self.m1
    
    @classmethod # specifies its a class method
    def getschool(cls): # as we are working with class and not instance therefore self
        return cls.school
    
    @staticmethod
    def info(): # static method
        print("This is student class")
    
    
        

s1=Student(14,64,75)
s2=Student(64,98,12)

# print(s1.get_m1()) # instance method
# print(s2.avg())
print(s1.getschool()) # class method
print(Student.getschool())

Student.info() # static method