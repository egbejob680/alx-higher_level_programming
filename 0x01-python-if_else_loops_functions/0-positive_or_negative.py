#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f'{number} is', end=' ')
if number > 0:
    print('positive')
elif number < 0:
    print('negative')
else:
    print('zero')
    