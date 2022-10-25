float1 = 1.1
float2 = 2.2
add = float1 + float2
print('Comparing floats:')
print(f'{float1} + {float2} = ' + str(add))
print('============')
print('Formatting float as String')
print(f'format({add}, ".2g") = ' + format(add, ".2g"))

print('Formatting as Math with tolerance')
tolerance = 0.00001
print(abs(float1 + float2) < tolerance)