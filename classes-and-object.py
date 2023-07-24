class Computer:# specifying class
    # attributes(properties) -> variable
    # behaviour() -> mehtods(functions)
    
    def config(self):
        print("i5,16gb,1TB")
    
comp1=Computer()# constructor
comp2=Computer()

comp1.config() # using object itself to call the object

Computer.config(comp1) # as there are many object for same class 
# therefore we need to the specify object
# here comp1 goes to self of config

a=5
a.bit_length

    