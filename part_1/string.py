name = 'Jorge'
surname = 'Reyes'
complete_name = name + ' ' + surname

print(f'Complete Name: {complete_name}')

# formatting text
placeholders = 'My name is: {} & my surname is: {}'.format(name, surname)
print(placeholders)

placeholders = f'My name is: {name} & my surname is: {surname}'
print(placeholders)