import random

print('Functions')


def my_func(num):
    number = num * random.randint(2, 5)
    print(f'Multiplication: {number}')


my_func(random.randint(10, 20))

print('+' * 50)


def my_func_return(num1, num2):
    number = num1 * num2
    return number


n = my_func_return(random.randint(10, 20), random.randint(100, 200))
print(f'Multiplication: {n}')

print('+' * 50)
print('Default values num1=1, num2=2')


def my_func_return(num1=1, num2=2):
    number = num1 * num2
    txt = 'The result is'
    return number, txt


# With parameters
n, t = my_func_return(random.randint(10, 20), random.randint(100, 200))
print(f'{t} = {n}')

# With no parameters
n1, t1 = my_func_return()
print(f'{t1} = {n1}')

# With Default parameters
n2, t2 = my_func_return(num2=100)
print(f'{t2} = {n2}')
