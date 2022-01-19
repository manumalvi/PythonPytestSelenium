# python Encapsulaton : wrapping up a data under a single unit.
# Its a protactive shield to prevent data from being accessed by the code outside this sheild.
# In this the variable or data of a calss is hidden from other class and can be access threw any other
# member function of own class in which they are declared .

# the main difference is Abstraction is implemented to hide unnecessary data and withdrawing relevant data.
# Whereas Encapsulation is the mechanism of hiding the code and the data together from the outside world or misuse.

# you can resitct access to menthod and varible
# can be achived by private varible and private methods

# private method / variable access in there own class start with 2 __ undersocre
# private variable access within class
'''
class Myclass:
    __a = 10

    def disp(self):
        print(self.__a)
myc = Myclass()
myc.disp()

#try this variable out side u will get error
print(Myclass.__a) # we cant assee its a private variable
'''
#####################################################################
'''
# private method can only accuss only within a method

class Myclass:
    def __disp1(self):
        print("Tihs is display method 1")

    def disp2(self):
        print("Tihs is display method 2")
        self.__disp1()

myc = Myclass()
myc.disp2()
#myc.__disp1()  # will throw error
'''
# Alternating way of using private methods
# we can access private variable outside of the class indirecly using methods
class MyClass:
    __empid=101

    def getempid(self,eid):
        self.__empid = eid
    def dispemp(self):
        print(self.__empid)

obj = MyClass()
obj.dispemp()
# you can change __empid value now
obj.getempid(105)
obj.dispemp()