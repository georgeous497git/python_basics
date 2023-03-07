print('Errors')

sum = lambda x, y: x + (y + 1)

assert sum(2, 2) == 4

age = 18

if age < 21:
    raise Exception('The age is not allowed')