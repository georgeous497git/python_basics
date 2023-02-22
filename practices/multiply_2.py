print('Multiplying each number by 2')

def multiply_numbers(numbers):
    return list(map(lambda n: n * 2, numbers))


numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)