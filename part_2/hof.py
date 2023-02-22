print('Higher Order Function')
import random

# EXAMPLE
# Assignment = lambda params: logic execution
# func_lambda = lambda num: num * num

# With a function as a parameter
# Assignment = lambda func_param: lambda function execution
func_lambda2 = lambda n, func: func(n)

print('*' * 60)

num = random.randint(56, 70)

# With a lambda function defined at the moment
result2 = func_lambda2(num, lambda n: n + 10)
print(f'Addition of 10 to {num = } is {result2 = }')
