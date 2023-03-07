print('Reading a File')

file = open('./read_file.txt')

print('Reading a File by line')
print(file.readline())

print('*' * 50)

print('Reading a File completely')
print(file.read())


print('Closing a File to save memory')
file.close()


print('*' * 50)

print('Closing a File automatically')

with open('./read_file.txt') as file:
    for line in file:
        print(line)
