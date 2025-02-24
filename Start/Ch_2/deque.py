# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters

# TODO: deques support the len() function

# TODO: deques can be iterated over

# TODO: manipulate items from either end

# TODO: use an index to get a particular item

"""
      <---h = popleft()     d [H       T] <- append(t)
              appendleft(t)->  [T       H] ---> h = pop()
"""

# initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# deques support the len() function
print("Item count: " + str(len(d)))

# deques can be iterated over
for elem in d:
    print(elem.upper())

# manipulate items from either end
d.pop()
d.popleft()
d.append(2)
d.appendleft(1)
print(d)

# use an index to get a particular item
print(d)
d.rotate(1)
print(d)

# OUT:
# $ python deque.py 
# Item count: 26
# A
# B
# C
# D
# E
# F
# G
# H
# I
# J
# K
# L
# M
# N
# O
# P
# Q
# R
# S
# T
# U
# V
# W
# X
# Y
# Z
# deque([1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2])
# deque([1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2])
# deque([2, 1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'])