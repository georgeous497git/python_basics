import functools


print('Reduce')
print('How to reduce an array')

numbers = [10, 20, 30, 40]

result = functools.reduce(lambda counter, item: counter + item, numbers)

print(f'{result = }')
