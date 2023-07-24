class Computer:
    def __init__(self):
        self.name="Naveen"
        self.age=28
        
    def update(self): # refers to the current object or instance
        self.age=54
        
    def compare(self,others):
        if self.age==others.age:
            return True
        else:
            return False

c1=Computer()
c2=Computer()

# all objects are created in heap memeory

# print(id(c1))
# print(id(c2))

# above is the address of objects in heap memory
# size of the object depends upon no of variables and size of the variable
# size is allocated to object by the constructor

# print(c1.name)
# c2.name="Anurag"
# c2.update()
# print(c2.age)

c2.age=89
if c1.compare(c2):
    print("they are same")
else:
    print("they are different")


 