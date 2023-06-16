
# adding arrays 
# [1,2,] + [1,3,2,] = [1,2,1,3,2]
# (1,2)+(1,3,) = (1,2,1,3)
# {1,2} + {3} : error unsupported
# [2] + (1) : error

# "*" operator
# *(a for a in range(20)) : 0-19
# *(lambda x: x**x) :error
# *(tuple) : tuple, *(1,2,3) : 1 2 3
# *{1,2,3} = 1 2 3 : unpacks
# *[1,2,3] = 1 2 3
# (1,2,3) * 2 = (1,2,3,1,2,3)
# [1,2,3] * 3 = [1,2,3,1,2,3,1,2,3]
# {} * 2 = error tho

# tuples
# a = 1,2,3 : (1,2,3)
# (1,23)*(2) = (1,23,1,23)
# (1,23)*(2,) : error bcos cannot multiply by tuple

# if you dont know how to cast 
# a = 1,2,3 :tuple
# b = [*a] : convert to list
# c = {*b}

# range() 
# range(start,stop,step)
# *range() unpacks to numbers and can be put in arrays
# {8,*range(5)}


"""

Certainly! Here are some lesser-known operations or implementations in Python regarding lists, tuples, sets, and other data structures:

List comprehension with conditional expressions: You can use conditional expressions within list comprehensions to filter elements based on certain conditions. For example:
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]

Set comprehension: Similar to list comprehensions, Python also supports set comprehensions for creating sets based on an iterable. For example:
numbers = [1, 2, 3, 4, 5, 6]
even_set = {x for x in numbers if x % 2 == 0}

Tuple unpacking: Python allows you to assign multiple variables at once using tuple unpacking. This can be handy when working with functions that return multiple values. For example:
name, age = ("John", 25)

Extended iterable unpacking: In addition to tuple unpacking, Python also supports extended iterable unpacking using the asterisk (*) operator. This allows you to assign multiple values to one variable or capture remaining values in a list. For example:
first, *rest = [1, 2, 3, 4, 5]

zip() function: The zip() function is used to combine multiple iterables into a single iterable of tuples. It stops when the shortest iterable is exhausted. For example:
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped = zip(names, ages)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

enumerate() function: The enumerate() function returns an iterator of tuples containing the index and value of elements in an iterable. This can be useful when you need both the index and value while iterating. For example:
names = ['Alice', 'Bob', 'Charlie']
for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")

collections.defaultdict: The defaultdict class from the collections module is a subclass of the built-in dict class. It provides a default value for keys that haven't been explicitly set, making it useful for counting or grouping elements. For example:
from collections import defaultdict

counts = defaultdict(int)
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

for fruit in fruits:
    counts[fruit] += 1

print(counts)  # {'apple': 3, 'banana': 2, 'orange': 1}
"""

from collections import Counter

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = Counter(fruits)

print(counts["apple"])  # Counter({'apple': 3, 'banana': 2, 'orange': 1})
