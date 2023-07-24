class Computer:

    def __init__(self,cpu,ram): # constructor
        self.cpu=cpu
        self.ram=ram
        
    
    def config(self):# passing the object
        print("config is",self.cpu,self.ram)
        
comp1=Computer('i5',16) # passing comp1,i5 and 16
comp2=Computer('ryzen',8)

comp1.config()
comp2.config()