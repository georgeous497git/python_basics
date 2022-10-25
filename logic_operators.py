print('Logic operators')
boolean1 = False
boolean2 = True
print('AND')
print(f'{boolean1} "and" {boolean2} = ' + str(boolean1 and boolean2))
print(f'{boolean1} "and" {boolean1} = ' + str(boolean1 and boolean1))
print(f'{boolean2} "and" {boolean2} = ' + str(boolean2 and boolean2))
print('OR')
print(f'{boolean1} "or" {boolean2} = ' + str(boolean1 or boolean2))
print(f'{boolean1} "or" {boolean1} = ' + str(boolean1 or boolean1))
print(f'{boolean2} "or" {boolean2} = ' + str(boolean2 or boolean2))
print('NOT')
print(f'not {boolean1} = ' + str(not boolean1))
print(f'not {boolean2} = ' + str(not boolean2))
