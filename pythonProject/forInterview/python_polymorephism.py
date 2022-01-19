# many use of same thing , many forms of same things
# one thing bihave in dfiff way

# method overriding : overding meand 2 methos same name but diff task

# overriding a variable
class Parent:
    name = "manu"
class Child(Parent):
    name = "malvi"
ob = Child()
print(ob.name)

# Override method # same methos performing diff jobs
class Bank:
    def rateofinterest(self):
        return 0
class Icici(Bank):
    def rateofinterest(self):
        return 10.5
ob = Icici()
print(ob.rateofinterest())

#overloading method

# same method is behaving diffently when we pass the name enad wehn we dont pass name
class Human:
    def sayHello(self,name=None):
        if name is not None:
            print("Hello"+ name)
        else:
            print("Hello")
hu = Human()
hu.sayHello("MANu")

#overloading method Example 2

# same method is behaving diffently when we pass the name enad wehn we dont pass name
class Bird:
    def fly(self,name=None):
        if name == "parrot":
            print("Can fly !!")
        if name == "penguin":
            print("Can not fly !!")
        if name == None:
            print("No input")
brd = Bird()
brd.fly("parrot")