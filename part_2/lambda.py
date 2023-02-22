print('Lambdas')

import random


# Function on their Basic Form
def increment(num):
    return num + 1


result = increment(random.randint(10, 15))
print(f'{result=}')

print('=' * 20)

# Lambda function

lambda_func = lambda num: num + 1

result = lambda_func(random.randint(10, 15))
print(f'{result=}')

print('=' * 20)

lambda_params = lambda num1, num2: f'The addition of {num1} + {num2} is: ' + str(num1 + num2)

num1 = random.randint(200, 300)
num2 = random.randint(200, 300)
add = lambda_params(num1, num2)
print(add)
