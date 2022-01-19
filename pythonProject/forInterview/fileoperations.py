'''
#simple read and close
file = open('data.txt')
print(file.read())
file.close()

#number of char you want to read
file = open('data.txt')
print(file.read(7))
file.close()

# read line by line
file = open('data.txt')
print(file.readline())
print(file.readline())
file.close()

# to read all line one by one
file = open('data.txt')
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()

# readlines will also behave like read but it will make a list of entire data
file = open('data.txt')
line = file.readlines()
print(line)
print(line[0])
for line in file.readines():
    print(line)

file.close()
'''

#write in file but read and close done by in one line
# read the file reverse the list and write it back
with open('data.txt', 'r') as reader:
    content = reader.readlines()
    print(content)
    content.reverse()
    print(content)
    with open('data.txt', 'w') as writer:
        for val in content:
            print(val)
            writer.write(val)
