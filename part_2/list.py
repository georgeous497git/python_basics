print('List Comprehension')

number = []
for n in range(0, 9):
    number.append(n * 2)
print(f'List: {number}')

numbers = [e * 2 for e in range(0, 9)]
print(f'List: {numbers}')

print('=====================================================')

number = []
for n in range(0, 9):
    if n % 2 == 0:
        number.append(n * 2)
print(f'List: {number}')

numbers = [e * 2 for e in range(0, 9) if e % 2 == 0]
print(f'List: {numbers}')