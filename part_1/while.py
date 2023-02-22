print("Loop 'while'")

index = 0

while index < 5:
    print(f'Index: {index}')
    index += 1
    if index == 3:
        break


print('===========================')

index = 0

while index < 5:
    index += 1
    if index < 4:
        continue
    print(f'Index2: {index}')




