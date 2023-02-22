import sys
import re
import time
import collections
print('Implementing Python modules')

print(f'{ sys.path = }')

text = 'My number is: 55 56 57 58 59'

coindicences = re.findall('[0-9]+', text)
print(f'{ coindicences = }')

timestamp = time.time()
timme = time.asctime(time.localtime())
print(f'{ timme = }')

number = [10, 20, 10, 30, 20, 40, 50]
counter = collections.Counter(number)
print(f'{ counter = }')