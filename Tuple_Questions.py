# nested tuple to store multiplication tables of 14 to 19, where each sub-tuple contains one table.
'''
Tuple = tuple(
    tuple(f"{num} * {i} = {num * i}" for i in range(1,11)) for num in range(14,20)
)
print(Tuple)
print(f"Length of the Tuple : {len(Tuple)}")
# Accessing specific multiplication table (e.g., table of 16)
table_of_16 = Tuple[2]  # 16 is the third number in the range 14-19
print(f"Multiplication Table of 16: {table_of_16}")

'''

# 1. Basics of Tuple
# What is a tuple in Python?
'''
Tuple: Tuple is an ordered , immutable collection of element enclose by parenthesis ().it can store duplicate value and multiple datatype value.
'''
# How is a tuple different from typing import Tuple
'''
1. Tuple (built-in type)
When you write tuple, you’re using Python’s built-in data type that stores an ordered, immutable sequence of elements.

Tuple from typing module:
not creating a real tuple — instead, you’re describing the type of a tuple for type hints (annotations).

ex:
from typing import Tuple

# 1️⃣ Using the built-in tuple
my_data = ("Mahadeb", 21, "India")
print(my_data)                 # ('Mahadeb', 21, 'India')
print(type(my_data))           # <class 'tuple'>

# 2️⃣ Using Tuple from typing (for type hinting)
def get_student_info() -> Tuple[str, int, str]:
    return ("Mahadeb", 21, "India")

# Function call
info = get_student_info()
print(info)                    # ('Mahadeb', 21, 'India')
print(type(info))              # <class 'tuple'>

reviced writng :
def get_student() -> Tuple[str,int,str]:
    return ("String Name", Any Numbers,"String Name")

'''

#Tuple Differ from a list?
'''
| Feature     | Tuple                    | List                 |
| ----------- | ------------------------ | -------------------- |
| Syntax      | `( )`                    | `[ ]`                |
| Mutability  | Immutable (can’t change) | Mutable (can change) |
| Performance | Faster                   | Slower               |
| Use case    | Fixed data               | Dynamic data         |

'''
# How do you create an empty tuple?
'''
empty_tuple = ()
print("This is empty tuple:",empty_tuple)

'''

# How do you create a tuple with a single element? Why is the comma important?
'''
name = ("Mahadeb Maity",)
print(f"Tuple only for single value , here comma is most important to create  single value tuple: Tuple is => {name} and their type is : {type(name)}")
'''

# Can a tuple store elements of different data types? Give an example.

# yes . tuple store multiple type of element . 
multiple_type_element = ("Mahadeb", 45, 56.50,True)
# print(multiple_type_element)

# How do you access elements of a tuple using indexing?
'''
print(multiple_type_element[2])
print(multiple_type_element[len(multiple_type_element)-1])
'''

# What is negative indexing in tuples? Give an example.
'''
nums = (10, 20, 30, 40)
print(nums[-1])  # 40
print(nums[-2])  # 30
'''
# What is tuple slicing? Show with example.
'''
Slicing returns a subtuple using the syntax tuple[start:end:step].
nums = (10, 20, 30, 40, 50)
print(nums[1:4])     # (20, 30, 40)
print(nums[::-1])    # (50, 40, 30, 20, 10)

'''
# What does it mean that tuples are immutable? Explain with an example.
'''
Once created, you can’t modify, add, or delete elements in a tuple.
nums = (1, 2, 3)
# nums[1] = 10 ❌ -> TypeError

'''
# Can you update or delete elements of a tuple? Why or why not?
'''
No — tuples are immutable.
You can only delete the entire tuple.
nums = (1, 2, 3)
# del nums[1] ❌
del nums       # ✅ deletes whole tuple

'''

# 2. Tuple Operations
# How do you concatenate two tuples?
'''
a = (1, 2)
b = (3, 4)
c = a + b
print(c)
# (1, 2, 3, 4)

'''
# How do you repeat a tuple multiple times?
'''
a = (1, 2)
print(a * 3)
# (1, 2, 1, 2, 1, 2)

'''
# How do you check if an element exists in a tuple? (in operator).
'''
a = (10, 20, 30)
print(20 in a)     # True
print(50 not in a) # True

'''
# How do you iterate through a tuple? (for loop, enumerate).
'''
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# With enumerate()
for i, color in enumerate(colors):
    print(i, color)

'''
# How do you unpack a tuple into variables?
'''
data = (10, 20, 30)
a, b, c = data
print(a, b, c)
# 10 20 30

'''
# What happens if the number of variables and tuple elements don’t match during unpacking?
'''
Python raises a ValueError.
a, b = (1, 2, 3)  # ❌ ValueError: too many values to unpack

'''
# 3. Tuple Functions & Methods
# What does len() return for a tuple?
'''
t = (10, 20, 30)
print(len(t))  # 3

'''
# How do you find the maximum and minimum value in a tuple?
# How do you find the sum of numeric tuple elements?
'''
t = (5, 10, 15)
print(max(t))  # 15
print(min(t))  # 5
print(sum(t))  # 30
'''
'''
# Explain .count() method with example.
t = (1, 2, 2, 3, 2)
print(t.count(2))  # 3
'''
# Explain .index() method with example.
'''
t = (10, 20, 30, 20)
print(t.index(20))  # 1
'''
# Can tuples be nested? How do you access nested elements?
'''
yes , 
t = (1, (2, 3), (4, 5))
print(t[1][1])  # 3

'''
# Can you convert a tuple to a list? Why would you do this?
# Can you convert a list to a tuple? Why would you do this?
'''
t = (1, 2, 3)
lst = list(t)   # tuple → list
t2 = tuple(lst) # list → tuple
'''

# 4. Tuple Packing & Unpacking
# What is tuple packing? Explain with an example.
# What is tuple unpacking? Show with example.
'''
Tuple Packing
Combining multiple values into one tuple.
packed = 10, 20, "Hi"
print(packed)
# (10, 20, 'Hi')

Tuple Unpacking
Extracting tuple elements into variables.
t = (1, 2, 3)
a, b, c = t
print(a, b, c)

'''
# What is extended unpacking (*) in tuples? Example:
'''
a, *b, c = (1, 2, 3, 4, 5)
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

'''
# a, *b, c = (1, 2, 3, 4, 5)
# What happens if you try unpacking with fewer or extra variables?
# unpacking mismatch , too many values unpack 

# 5. Advanced / Special Topics
# Can a tuple contain mutable objects (like list, dict)? Example: (1, [2,3]).
# What happens if you modify a list inside a tuple?
'''
t = (1, [2, 3])
t[1].append(4)
print(t)
# (1, [2, 3, 4])
The tuple itself is immutable, but the list inside it can change.

'''
# Can a tuple be used as a dictionary key? Why?
'''
Yes, if all its elements are immutable.
d = {(1, 2): "Point A"}
print(d[(1, 2)])  # Point A

'''
# Can a tuple be added to a set? Why or why not?
'''
Yes, but only if it contains immutable elements.
s = {(1, 2), (3, 4)}
print(s)

'''
# How does Python internally store tuples compared to lists (memory & performance)?
'''
Tuples are stored in a fixed-size memory (static), lists use dynamic arrays.
✅ Tuples are faster and use less memory.

'''
# Explain why tuples are hashable but lists are not.
'''
Hashing requires immutable content.
Lists can change → ❌ not hashable.
Tuples can’t change → ✅ hashable.
'''
# What is the difference between shallow copy and deep copy in context of tuples?
'''
Shallow copy: creates new reference (not a deep copy since tuples are immutable).

Deep copy: only relevant if tuple contains mutable objects.

import copy
t1 = (1, [2, 3])
t2 = copy.deepcopy(t1)
t2[1].append(4)
print(t1)  # (1, [2, 3])
print(t2)  # (1, [2, 3, 4])
'''
# What is a tuple constructor (tuple()) and how does it work?
'''
tuple() converts an iterable into a tuple.

t = tuple([1, 2, 3])
print(t)
# (1, 2, 3)
'''
# 🔹 6. Tuple in Real Problems
# How do you return multiple values from a function using a tuple?
'''
def get_info():
    return ("Mahadeb",22)

Name , Age = get_info()
print(Name, Age)
'''

# How can you swap two variables using tuple unpacking?
'''
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5

'''
# How do you zip two tuples together?
'''
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5
'''
# How do you convert a string into a tuple of characters?
'''
Name = "Maahdeb"
print(tuple(Name))
'''

# How do you create a tuple from a dictionary? (keys/values/items).
'''
Info ={
    "Name" : "Mahadeb Maity",
    "Age" : 22,
    "Education" : "Graduation"
}
print(tuple(Info.keys()))
print(tuple(Info.values()))
print(tuple(Info.items()))
'''

# How to flatten a nested tuple?
'''
t = (1, (2, 3), (4, 5))
flat = tuple(x for sub in t for x in (sub if isinstance(sub, tuple) else (sub,)))
print(flat)
# (1, 2, 3, 4, 5)

'''
# How do you find duplicate elements in a tuple?
'''
t = (1, 2, 3, 2, 4, 1)
duplicates = tuple(set([x for x in t if t.count(x) > 1]))
print(duplicates)
# (1, 2)
'''
# How do you sort elements of a tuple?
'''
t = (5, 2, 8, 1)
sorted_tuple = tuple(sorted(t))
print(sorted_tuple)
# (1, 2, 5, 8)

'''
# How do you reverse a tuple?
'''
t = (1, 2, 3)
print(t[::-1])
# (3, 2, 1)

'''

# 7. Tricky / Interview Level

# What is the difference between (1) and (1,)?
# What is the output of this:
# t = (1,2,[3,4])
# t[2].append(5)
# print(t)

# Why is tuple faster than list?
'''
1️⃣ Why is tuple faster than list?
✅ Reason:

Tuples are immutable → their contents cannot change after creation.

Lists are mutable → they allow adding, removing, and modifying elements.

Because of this:

Python can optimize memory storage and iteration speed for tuples.

No need to allocate extra space or manage dynamic resizing (which lists require).

⚙️ Example:
import timeit

print(timeit.timeit("(1, 2, 3, 4, 5)", number=1000000))   # tuple creation
print(timeit.timeit("[1, 2, 3, 4, 5]", number=1000000))   # list creation


💡 Result:
The tuple version usually runs faster than the list version.
'''
# What happens if you use + or * with tuples?
'''
➕ 2️⃣ What happens if you use + or * with tuples?
🧩 Tuple concatenation (+)

Combines two tuples into a new one.

Example:

a = (1, 2, 3)
b = (4, 5)
print(a + b)   # (1, 2, 3, 4, 5)

✖️ Tuple repetition (*)

Repeats the tuple elements.

Example:

a = (1, 2)
print(a * 3)   # (1, 2, 1, 2, 1, 2)

⚠️ Important:

These operations create new tuples — since tuples are immutable, the original tuples are not changed.
'''
# Can tuple comprehension exist in Python? If not, then what happens?
'''
No,
3️⃣ Can tuple comprehension exist in Python?
❌ No, tuple comprehension does not exist.

If you try:

t = (x**2 for x in range(5))
print(t)


You get:

<generator object <genexpr> at 0x...>


👉 This means Python creates a generator, not a tuple.

✅ To make it a tuple:

You must explicitly convert it:

t = tuple(x**2 for x in range(5))
print(t)   # (0, 1, 4, 9, 16)
'''


