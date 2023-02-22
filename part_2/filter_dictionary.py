print('Dictionary Filter')
print('+' * 50)

matches = [
    {
        'team': 'team01',
        'wins': 1
    },
    {
        'team': 'team02',
        'wins': 5
    },
    {
        'team': 'team03',
        'wins': 3
    },
    {
        'team': 'team04',
        'wins': 8
    }
]

print(f'{matches = }')

list = list(filter(lambda i: i['wins'] > 3, matches))
print('Filtering...')
print(f'{list = }')