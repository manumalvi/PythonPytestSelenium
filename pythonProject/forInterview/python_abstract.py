# Abstract class are class that contain one or more method
# Abstract method is method that is declared but  contain one no implimention
# Abstract class cant be instanciated and require subclass to provide implimentaion for abstrct method

#in python ABC is pre defiend abstact class
from abc import  ABC , abstractmethod
'''
class A(ABC):  #now this become abstract class
    @abstractmethod
    def display(self):
        None

class B(A):
    def display(self):
        print("This is display method !! ")

oj = B()
oj.display()
'''
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
class Tiger():
    def eat(self):
        print("Eat NON VEG")
class Cow():
    def eat(self):
        print("Eat Veg")

t=Tiger()
t.eat()
c=Cow()
c.eat()