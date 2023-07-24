# polymorphism is poly = many and morphism = forms

# Duck typing
class PyCharm:
    def execute(self):
        print("compiling")
        print("running")
    
class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("compiling")
        print("running")
    
class Laptop:
    def code(self,ide):
        ide.execute()

lap1=Laptop()
ide=MyEditor()
lap1.code(ide)    
 