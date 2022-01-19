def sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)

#sum(1,2,5)

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
