# Demonstrate the usage of defaultdict objects

from collections import defaultdict
from typing import DefaultDict

# define a list of items that we want to count
fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']

# # TODO: use a dictionary to count each element
# fruitCounter = dict()

# # TODO: Count the elements in the list
# for fruit in fruits:
#     fruitCounter[fruit] += 1

# # TODO: print the result

# use a dictionary to count each element
fruitCounter: DefaultDict[str, int] = defaultdict(int)    # freq of each fruit

# Count the elements in the list
for fruit in fruits:
    fruitCounter[fruit] += 1
#

# print the result
for (k, v) in fruitCounter.items():
    print(k + ": " + str(v))
#

# OUT:
# $ python defaultdict.py 
# apple: 2
# pear: 1
# orange: 1
# banana: 3
# grape: 1