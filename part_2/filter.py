print('Filter')

numbers = [10, 20, 30, 40, 50, 60]
third = filter(lambda x: x % 3 == 0, numbers)
list = list(third)
print(f'Evens: {list}')

print('+' * 50)