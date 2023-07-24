# two method with different parameters (method overloading)
# two methods with same name,class,number of parameters (method overriding)

class Student:
    def __init__(self,m1,m2) -> None:
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None): # method overloading as python does not allow 
        # multiple methods with same name
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif  a!=None and b!=None :
            s=a+b
        else:
            s=a
        return s
    
    def show(self):
        print("in A show")

class B(Student):
    def show(self): # overriding show method of A
        print("in B show")


s1=B(83,18)

s1.show()
