# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# TODO: Create a Counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)
# TODO: How many students in class 1 named James?
print(c1["James"])

# TODO: How many students are in class 1?
print(sum(c1.values()))

# TODO: Combine the two classes
# Combine the two classes
c1.update(class2) # merge/update c1 w/ c2 members
print(sum(c1.values()), "students in class 1 and 2")

# TODO: What's the most common name in the two classes?
print(c1.most_common(3))

# TODO: Separate the classes again
c1.subtract(class2)
print(c1.most_common(1))
# TODO: What's common between the two classes?
print(c1 & c2)  # c1 and c2 (intersection)

# OUT:
# $ python counter.py
# 2
# 12
# 24 students in class 1 and 2
# [('James', 3), ('Frank', 2), ('Bob', 1)]
# [('James', 2)]
# Counter({'James': 1, 'Frank': 1})