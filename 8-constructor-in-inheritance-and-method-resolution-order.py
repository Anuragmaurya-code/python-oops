class A: 
    def __init__(self) -> None:
        print("in A init")
        
    def feature1(self):
        print("Feature 1 is working")
        
    def feature2(self):
        print("Feature 3 is working")

class B(): 
    
    def __init__(self) -> None: # now it wont run the init function of A
        # super().__init__() # for calling super class function init
        print("in B init")
        
    def feature3(self):
        print("Feature 3 is working")
        
    def feature4(self):
        print("Feature 4 is working")
 
# for multiple super class it will consider class from left to right as superclass
# there here method resolution order (left -> right)       
class C(A,B):
    def __init__(self) -> None:
        super().__init__()
        print("in C init")
        
    def feat(self):
        super().feature4() # super can be used to call parent class method
c=C()
c.feat()