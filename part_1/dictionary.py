print('Dictionary')

dictionary = {}
print('Original = ' + str(dictionary))

dictionary = {
    'key0': 'value0',
    'key1': 'value1'
}
print('Dictionary = ' + str(dictionary))
print('Length = ' + str(len(dictionary)))

print("Value of 'key0' = " + str(dictionary['key0']))
print("Getting value of 'key1' = " + str(dictionary.get('key1')))

print("Contains value 'value3' in dictionary = " + str('value3' in dictionary))

print('====================================================')
print('Dictionary Operations')

f1_vehicle = {
    'brand': 'Red Bull',
    'hp': '580',
    'torque': '45',
    'tires': ['soft'],
    'pilot': 'Checo'
}

print('Original F1 = ' + str(f1_vehicle))
f1_vehicle['hp'] = '600'
print("Updating value in key 'hp' = " + str(f1_vehicle))
f1_vehicle['tires'].append('medium')
print("Adding a tire = " + str(f1_vehicle))

print("Eliminating an attribute from Dictionary (Option 1)")
del f1_vehicle['pilot']
print("Result = " + str(f1_vehicle))

print("Eliminating an attribute from Dictionary (Option 2)")
f1_vehicle.pop('torque')
print("Result = " + str(f1_vehicle))

print("Getting items from Dictionary")
print("Result = " + str(f1_vehicle.items()))

print("Getting keys from Dictionary")
print("Result = " + str(f1_vehicle.keys()))

print("Getting values from Dictionary")
print("Result = " + str(f1_vehicle.values()))


