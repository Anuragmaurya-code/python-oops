# subclass can access all the features of superclass  but vice versa is not true
class A: # superclass or parent class
    def feature1(self):
        print("Feature 1 is working")
        
    def feature2(self):
        print("Feature 3 is working")

class B(A): # inheriting features of A / sub class or child class / single level inheritance
    def feature3(self):
        print("Feature 3 is working")
        
    def feature4(self):
        print("Feature 4 is working")
    
class C(B): # multi level inheritance
    def feature5(self):
        print("Feature 5 is working")

class E():
    def feature6(self):
        print("Feature 6 is working")

class F(C,E): #multiple level inheritance
    def feature7(self):
        print("Feature 7 is working")
        
        
    
a1=A()
a1.feature1()
b1=B()
b1.feature1()
c1=C()
