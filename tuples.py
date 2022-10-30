print('Using tuples')

numbers = (100, 200, 300, 400, 100)
print('Tuple = ' + str(numbers))
print('Type = ' + str(type(numbers)))
print('Specific location 2 = ' + str(numbers[2]))

print('Getting from index = ' + str(numbers.index(400)))
print('Counting elements = ' + str(numbers.count(100)))

list_from_tuple = list(numbers)
print('Tuple to List = ' + str(list_from_tuple))
tuple_from_list = tuple(list_from_tuple)
print('List to Tuple = ' + str(tuple_from_list))
