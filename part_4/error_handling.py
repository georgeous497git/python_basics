print('Errors Handling')

try:
    num = 0 / 0
except ZeroDivisionError as e:
    print('Error Caught => ', e)



try:
    num = 0 / 0
except Exception as e:
    print('Generic Exception => ', e)


try:
    num = 0 / 0
    assert 1 != 1
except ZeroDivisionError as e:
    print('Error => ', e)
except Exception as e:
    print('Error => ', e)