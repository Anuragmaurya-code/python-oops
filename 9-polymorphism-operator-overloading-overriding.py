
# a=5
# b=6
# print(a+b)
# print(int.__add__(a,b))

class Student:
    def __init__(self,m1,m2) -> None:
        self.m1=m1
        self.m2=m2
    def __add__(self,other): # overloading add methods with different type of parameters
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
    def __gt__(self,other):
        r1 =self.m1+self.m2
        r2 =other.m1+other.m2
        return r1>r2
    def __str__(self):# overriding the buildin function str
        return f'{self.m1} {self.m2}'

s1=Student(38,29)
s2=Student(22,39)

# s3=s1+s2
# if s1>s2:
#     print("s1 is greater")
# else:
#     print("s2 is greater")

print(s1)

        