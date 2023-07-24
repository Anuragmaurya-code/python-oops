class Student: # outer class
    def __init__(self,name,rollno) -> None:
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
        
    def show(self):
        print(self.name,self.rollno)
        
    class Laptop: # Inner class
        def __init__(self) -> None:
            self.brand='HP'
            self.cpu='i5'
            self.ram=12
        def show(self):
            print(self.brand,self.cpu,self.ram)
            

s1=Student('Anurag',23)
s2=Student('Sahil',24)

s1.show() # outer class
s1.lap.show() # inner class

        