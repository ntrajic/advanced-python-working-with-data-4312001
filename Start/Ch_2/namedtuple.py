# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple

# TODO: use _replace to create a new instance


# create a Point namedtuple
Point = collections.namedtuple("Point", "x y")

p1 = Point(10, 20)
p2 = Point(30, 40)

print(p1, p2)
print(p1.x, p1.y)

# use _replace to create a new instance
p1 = p1._replace(x=100)
print(p1)

# OUT:
# $ python namedtuple.py 
# Point(x=10, y=20) Point(x=30, y=40)
# 10 20
# Point(x=100, y=20)