print("Using Lists")
numbers = [1, 3, 5, 7]
print("Printing a list of numbers: " + str(numbers))

strings = ['Cartucho', 'Chispita', 'Rufo']
print("Printing a list of strings: " + str(strings))

manyTypes = [10, True, "Language"]
print("Printing a list of many types: " + str(manyTypes))

manyTypes = [10, True, "Language"]
print("Printing the position 1 of the list: " + str(manyTypes[1]))

print(f"Updating the location 0 & 1 in the list: {manyTypes}")
manyTypes[0] = "Python"
manyTypes[1] = "Programming"
print(f"=>: {manyTypes}")

print('Slicing a list from 0 to 1 => ' + str(manyTypes[:1]))
print('Checking if list contains "Java" value => ' + str("Java" in manyTypes))