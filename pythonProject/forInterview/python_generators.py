# diff btw return and yield is returm ends the function one it returns the value but with yield
#function wont end it gets pause
# genetetaor returns iterator object

def evenNumbers(n):
    i=1
    while n:
        yield i*2
        i = i + 1
        n = n -1

it = evenNumbers(10)
print(next(it))
print(next(it))
print(next(it))
# new = []
# while True:
#     try:
#         new.append(next(it))
#     except StopIteration:
#         break
# print(new)
