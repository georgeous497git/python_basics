print("Lists Operations")

numbers = [0, 2, 3, 5, 6, 7]
print(f'Original = {numbers}')

print("Updating the list")
numbers[-1] = 8
print(f'Result = {numbers}')

print("Adding to the list")
numbers.append(10)
print(f'Result = {numbers}')

print("Inserting at specific location")
numbers.insert(1, 1)
print(f'Result = {numbers}')

print("Fusing two lists")
texts = ['num1', 'num2', 'num3', 'num4']
lists = texts + numbers
print(f'Result = {lists}')

print("Inserting at specific index")
index = texts.index('num2')
texts[index] = 'NUM_2'
print(f'Result = {texts}')

print("Removing an element")
texts.remove('num1')
print(f'Result = {texts}')

print("Popping an element")
texts.pop()
print(f'Result = {texts}')

print("Popping an element from specific location")
texts.pop(0)
print(f'Result = {texts}')

print("Reversing a list")
numbers.reverse()
print(f'Result = {numbers}')

print("Sorting a list")
nums = [100, 500, 800, 400, 700]
numbers.reverse()
print(f'Result = {nums}')



