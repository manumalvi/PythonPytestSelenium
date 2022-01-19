# there are 2 ways to handle error in python
# exception and assert

cartItem = 0
'''
Method 1 
if cartItem != 2:
    raise Exception("cart Item not match !")

Method 2 
assert(cartItem == 2)  # this condition should always true else it will assert always
'''
######################
# this is human writter error in except
try:
    with open('sfgsdfg.txt', 'r') as reader:
        reader.read()
except:
    print("There is some error!!")

############################3
# what error system throw
try:
    with open('sfgsdfg.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

###############################
# finally block will always execute where it has error (control go to except) or not
try:
    with open('sfgsdfg.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("clear resurces !!")