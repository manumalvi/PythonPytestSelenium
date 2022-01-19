
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x,k = map(int,input().split())
    i = 1
    new = 0
    while i < k:
        new = new + (x ** i)
        i = i + 1
    new = new+1
    if new == k:
        print("True")
    else:
        print("False")
