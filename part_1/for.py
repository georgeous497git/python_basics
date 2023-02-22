print('For Loop')

for e in range(5, 9):
    print(e)

print('===========================')

list = [100, 200, 300]
for e in list:
    print(e)

print('===========================')

tuple = (100, 200, 300)
for e in tuple:
    print(e)

print('===========================')

f1_vehicle = {
    'brand': 'Red Bull',
    'hp': '580',
    'torque': '45',
    'tires': ['soft'],
    'pilot': 'Checo'
}
for e in f1_vehicle:
    print(e)

print('===========================')

for e in f1_vehicle:
    print(f1_vehicle[e])

print('===========================')

for k, v in f1_vehicle.items():
    print(f'Key = {k} - Value = {v}')

print('===========================')

f1_vehicle2 = {
    'brand': 'Red Bull',
    'hp': '580',
    'torque': '45',
    'tires': ['soft'],
    'pilot': 'Checo'
}

vehicles = [
    f1_vehicle,
    f1_vehicle2
]


for vehicle in vehicles:
    print(f'Vehicle = {vehicle}')