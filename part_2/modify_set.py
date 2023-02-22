print('Modify Set')

set_text = {'movies', 'popcorn', 'candy'}
print(f'Original Set {set_text}')
size = len(set_text)
print(f'Size Set {size}')

print(f"'movies' is in set = {'movies' in set_text}")

print('Adding elements')
set_text.add('soda')
print(f'Modified Set {set_text}')

print('Updating elements')
set_text.update({'seat', 'projector'})
print(f'Modified Set {set_text}')

print('Removing elements if exists')
set_text.remove('soda')
print(f'Modified Set {set_text}')

print('Removing elements')
set_text.discard('soda')
print(f'Modified Set {set_text}')

print('Removing elements')
set_text.pop()
print(f'Modified Set {set_text}')

print('Cleaning elements')
set_text.clear()
print(f'Modified Set {set_text}')











