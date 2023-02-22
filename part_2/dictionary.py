print('Dictionary Comprehension')

number = {}
for n in range(0, 9):
    number[n] = n * 2
print(f'Dictionary: {number}')

numbers = {e: e * 2 for e in range(0, 9)}
print(f'Dictionary: {numbers}')

print('=====================================================')

numbers = {e: e * 2 for e in range(0, 9) if e % 2 == 0}
print(f'Dictionary: {numbers}')

print('=====================================================')

names = ['pepito', 'pablito', 'juanito']
ages = [35, 36, 37]

map = {n: ages.pop() for n in names}
print(f'Dictionary: {map}')

print('=====================================================')

names = ['pepito', 'pablito', 'juanito']
ages = [35, 36, 37]

map2 = {n: a for (n, a) in zip(names, ages)}
print(f'Dictionary: {map2}')

print('=====================================================')

names = ['pepito', 'pablito', 'juanito']
ages = [35, 36, 37]

map2 = {n: a for (n, a) in zip(names, ages) if a > 35}
print(f'Dictionary: {map2}')

