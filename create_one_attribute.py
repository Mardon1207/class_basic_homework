#Create a "Person" class
#Create an attribute "name" in the "Person" class
class Person:
    name="Mardon"
    def __init__(self,n):
        self.name=n
x=Person("Mardon")
print(x.name)