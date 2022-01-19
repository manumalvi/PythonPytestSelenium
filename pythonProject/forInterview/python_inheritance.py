'''INheritance in python '''
'''
class Parent():
    def func1(self):
        print("This is parent class")

class Child(Parent):
    def func2(self):
        print("this is a child Function")

ob = Child()
ob.func1()
ob.func2()
'''
# __init__() function is called automaticlly every time the class is used to create an object
# override parent class init method using child class
'''
class Parent():
    def __init__(self,fname,fage):
        self.name = fname
        self.age = fage
    def viwe(self):
        print(self.name,self.age)

class Child():
    def __init__(self,fname,fage):
        Parent.__init__(self,fname,fage)
        self.lastname = "manu"
    def view(self):
        print(self.age,self.lastname,self.name)

ob = Child(23,"python")
ob.view()
'''
'''
# type of Inheritance in pyhon Single , muliple , multi level , herarcial
# single inheritance : one parent and one object
# multiple inheritance : more then one parent class and child class is taking from all of them
# multilevel : eg one parent class one cild class but now this child class in parent for next child class
#hirarchical : more than one type of inheritance

# multiple inheritance
class Parent1():
    def func1(self):
        print("This is parent 1 class")

class Parent2():
    def func2(self):
        print("This is parent 2 class")

class Child(Parent1,Parent2):
    def func3(self):
        print("this is a child Function")

ob = Child()
ob.func1()
ob.func2()
'''
'''
# multilevel inheritance
class Parent1():
    def func1(self):
        print("This is parent 1 class")

class Parent2(Parent1):
    def func2(self):
        print("This is parent 2 class")

class Child(Parent2):
    def func3(self):
        print("this is a child Function")

ob = Child()
ob.func1()
ob.func2()
'''
# herarchical inheritnace
'''
class Parent1():
    def func1(self):
        print("This is parent 1 class")

class Parent2(Parent1):
    def func2(self):
        print("This is parent 2 class")

class Child(Parent1):
    def func3(self):
        print("this is a child Function")

ob = Child()
ob1 = Parent2()
ob.func1()
ob1.func1()
'''
'''
# super function
# Super function direclty call the parent class method
class Parent():
    def func1(self):
        print("This is parent class")

class Child(Parent):
    def func2(self):
        super().func1()
        print("this is a child Function")

ob = Child()
ob.func2()
'''
# Method Overridding can be achived to change functionality of parent class
class Parent():
    def func1(self):
        print("This is function 1  class")

class Child(Parent):
    def func1(self):
        print("This is function 2 class")

ob = Child()
ob.func1()
