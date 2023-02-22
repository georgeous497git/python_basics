print('Map')
print('How to transform (map) a given list')

numbers = [10, 20, 30, 40]
numbers_2 = []

# Reference logic
for ix in numbers:
    numbers_2.append(ix * 2)

print(f'{numbers_2 = }')

numbers_3 = map(lambda e: e * 2, numbers)

print(f'{list(numbers_3) = }')

print('*' * 60)

data = [
    {
        'name': 'J',
        'age': 50
    },
    {
        'name': 'F',
        'age': 40
    }
]

names = map(lambda i: i['name'], data)

print(f'{list(names) = } from {data = }')


def add_att(obj):
    new_obj = obj.copy()
    new_obj['both'] = new_attr(new_obj)
    return new_obj


new_attr = lambda n: n['name'] + str(n['age'])

new_data = map(lambda d: add_att(d), data)
print(f'{list(new_data) = } from {data = }')
