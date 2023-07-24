# types of variable is instance and class variable

class Car:
    wheels=4 # class variable (change in it affect other objects too )
    
    def __init__(self) -> None: # variable inside init are instance variable
        self.mil=10 # instance variable is different for different object and its
        # change in value does not affect other objects  
        self.com="BMW"
        
car1=Car()
car2=Car()

car2.mil=20 #changing instance variable
Car.wheels=5 # changing class variable

print(car1.mil,car1.com,car1.wheels)
print(car2.mil,car2.com,car2.wheels)