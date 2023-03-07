print('Writing a File')

print('Permission r+ = read & write')
print('Permission w+ = delete & write')


with open('./read_file.txt', 'r+') as file:
    file.write('a new line\n')
    for line in file:
        print(line)

