# 1. Basics of List
# What is a list in Python? How is it different from arrays in other languages?
'''
A List  in python is a Collection of various data types items that is ordered and mutable (can be change after creation ). 
it is allow duplicate itmes . List are most powerful data structure in python which are used to store multiple data types items in a single variable.
We can create list by using square brackets [] of using list() constructor.

Syntax: list_name = [item1, item2, item3, ...]

Example of list : items = [1, "Hello", 3.14, True, [1,2,3]] # store multiple data types items in a single variable .

Lists are different from arrays in other languages in following ways:
1. Heterogeneous: Lists can store items of different data types, whereas arrays typically store items of the same data type.
2. Dynamic Sizing: Lists can grow and shrink in size dynamically, while arrays have a fixed size once created.
3. Built-in Methods: Python lists come with a variety of built-in methods for manipulation, making them more versatile than traditional arrays Because
Arrays in other languages usually require manual handling for such operations.

'''
# How do you create an empty list? Give examples.
'''
empty_list1 = [] # Using square brackets
empty_list2 = list() # Using list() Constructor
print(empty_list1,type(empty_list1))
print(empty_list2,type(empty_list2))
'''
# How do you create a list with mixed data types?
'''
Mixed_Datatype_items_list = [1,"Hello",3.14,True,[1,2,3]]
print(Mixed_Datatype_items_list,type(Mixed_Datatype_items_list))
'''
# How do you access elements of a list using indexing?
'''
List_Element = [1,2,3,4,5]
print(f"List elements : {List_Element}")
print(f"Accessing the first element : {List_Element[0]}") 
print(f"Accessing the last element : {List_Element[len(List_Element)-1]}") 
print(f"Accessing the last element using negative indexing : {List_Element[-1]}") 
'''
# What is negative indexing in lists? Explain with an example.
'''
Negative indexing allows you to access list elements from the end of the list. The last element is at index -1, the second last at -2, and so on.

Example:
List_Element = [1, 2, 3, 4, 5]
print(f"Accessing the last element using negative indexing : {List_Element[-1]}")
'''


# How do you find the length of a list?
''' 
using len() function we can find the length of a list.
example:
List = [ 1,2,3,4,5]
print(len(List))
'''

# How do you update or change an element in a list?
# Explain list mutability with examples.
# same answer as above question
'''
using indexing we can update or change an element in a list.
List_Element = [1, 2, 3, 4, 5]
List_Element[2] = 10 # changing the 3rd element (index 2) to 10
print(f"Updated List : {List_Element}")
'''

# 🔹 2. List Operations
# How do you concatenate two lists?
'''
List1 = [1, 2, 3,3,2]
List2 = [4, 5, 6,4,5]
Concatenated_List = List1 + List2
print(f"Concatenated List : {Concatenated_List}")
'''

# How do you repeat a list multiple times?
'''
List1 = [1, 2, 3]
Repeated_List = List1 * 3
print(f"Repeated List : {Repeated_List}")
'''

# How do you check if an element exists in a list? (in operator)
'''
List1 = [1, 2, 3, 4, 5]
if 3 in List1:
    print("Element found")
else:
    print("Element not found")
'''

# How do you iterate over a list using for loop?
'''
List1 = [1, 2, 3, 4, 5]
for item in List1:
    print(f"Item: {item}")
'''

# How do you slice a list? Explain with examples (list[start:end:step]).
# Here, List1[start:end:step] is the slicing syntax.
'''
using slicing we can access a range/ part of elements from a list.
Example:
List1 = [1, 2, 3, 4, 5]
print(List1[1:4]) # Output: [2, 3, 4]
print(List1[:3])  # Output: [1, 2, 3]
print(List1[::-1]) # Output: [5, 4, 3, 2, 1]
'''

# What is list unpacking? Give an example.
'''
List unpacking in python is a feature that assigns element of a list to multiple variables in a single statement.
Example:
List1 = [1, 2, 3]
a,b,c = List1
print(a+b+c) # Output: 6
print(f"a: {a}, b: {b}, c: {c}")
'''

# 🔹 3. List Methods
# Explain and use .append() method.
'''
append() method is used to add an element at the end of the list.
Example:
Fruits = ["apple", "banana", "cherry"]
Fruits.append("orange")
print(Fruits) # Output: ['apple', 'banana', 'cherry', 'orange']
'''

# Explain and use .extend() method. How is it different from append?
'''
Extend() method is used to add multiple elements from distro import like
from an iterable (like another list) to the end of the list.
Example: 
Fruits = ["apple", "banana", "cherry"]
Fruits.extend(["orange", "grape"])
print(Fruits) # Output: ['apple', 'banana', 'cherry', 'orange', 'grape']
# Difference between append() and extend():
# append() adds a single element to the end of the list, while extend() adds multiple elements from an iterable to the end of the list.
'''

# Explain .insert(index, value) with an example.
'''
Insert() method is used to add an element at a specific index in the list.
Example:
Fruits = ["apple", "banana", "cherry"]
Fruits.insert(1, "orange") # Inserting "orange" at index 1
print(Fruits) # Output: ['apple', 'orange', 'banana', 'cherry']
'''
# How do you remove an element using .pop()? What does it return?
'''
Pop() method is used to remove an element at a specific index (default is the last element) and return it.
Example:
Fruits = ["apple", "banana", "cherry"]
removed_fruit = Fruits.pop(1) # Removing element at index 1
print(Fruits) # Output: ['apple', 'cherry']
print(removed_fruit) # Output: 'banana'
'''

# How do you remove an element using .remove()?
'''
Remove() method is used to remove the first occurrence of a specific value from the list.
Example:

Fruits = ["apple", "banana", "cherry"]
Fruits.remove("banana")
print(Fruits) # Output: ['apple', 'cherry']
'''

# Difference between .pop() and .remove()?
'''
pop() removes an element by index and returns it, while remove() removes an element by value and does not return it.
'''
# What does .clear() do?
'''
clear() method is used to remove all elements from the list, making it empty.
Example:
Fruits = ["apple", "banana", "cherry"]
Fruits.clear()
print(Fruits) # Output: []

'''

# How do you copy a list (copy() vs = assignment)?
'''
# we can copy element into a list by using copy() method or using assignment operator (=).
list1 = [1, 2, 3]
copy_List = list1.copy() # using copy() method
copy_List.append(4) # modifying copy_List
print(f"Original List: {list1}")
print(f"Temporary List: {copy_List}")

list2 = [4, 5, 6]
assigned_List = list2 # using assignment operator (=)
assigned_List.append(7) # modifying assigned_List
# Both list2 and assigned_List will reflect this change.
print(f"Original List: {list2}")
print(f"Assigned List: {assigned_List}")
# Both list2 and assigned_List refer to the same object in memory.
# So, changing one also changes the other.
# 👉 This is shallow assignment, not a true copy.

'''

# Explain .count() with an example.
'''
count() method is used to count the number of occurrences of a specific value in the list.
Example:
Fruits = ["apple", "banana", "cherry", "apple"]
apple_count = Fruits.count("apple")
print(apple_count) # Output: 2
'''
    
# Explain .index() with an example.
'''
index() method is used to find the first occurrence of a specific value in the list and return its index.
Example:
Fruits = ["apple", "banana", "cherry"]
banana_index = Fruits.index("banana")
print(banana_index) # Output: 1
'''

# How do you reverse a list (.reverse() vs slicing [::-1])?
'''
list1 = [1, 2, 3, 4, 5]
list1.reverse()
print(list1)
# Key points:
#     .reverse() modifies the original list in place.
#     It does not return a new list (returns None).
#     Good if you don't need the original order anymore.

list1 = [1, 2, 3, 4, 5]
reversed_list = list1[::-1]
print( "Original List:", list1)
print( "Reversed List:", reversed_list)
# Key points:
#     Slicing [::-1] creates a new reversed list.
#     The original list remains unchanged.
#     Good if you want to keep both original and reversed versions.
'''

# How do you sort a list (.sort() vs sorted())? Explain differences.
'''
list1 = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(list1)
print("Original List:", list1)
print("Sorted List using sorted():", sorted_list)
# Key points:
    # sorted() creates a new list and leaves the original unchanged.
    # Works on any iterable (list, tuple, string, dictionary keys, etc.).
    # More flexible if you need both the original and sorted version.

List2 = [3, 6, 1, 8, 2]
List2.sort()
print("Sorted List using .sort():", List2)
# Key points:
    # .sort() works in-place (modifies the original list).
    # It returns None, not a new list.
    # More memory efficient (no new list created).
    # Only works on lists (not tuples, sets, etc.).

# If How to sort list as a decending order?

# List1 = [5, 2, 9, 1, 5, 6]
# List3 = List1.sort(reverse=True)
# List2 = sorted(List1, reverse=True)
# print("List sorted in descending order using .sort():", List3) # return None value  So 
# print("Original List after .sort():", List1) # Original list is changed and reversed 
# print("List sorted in descending order using sorted():", List2)
'''

# Extra concept: 
'''
# key parameter in sort() and sorted():
Fruits = ["banana", "apple", "cherry", "date"]
Fruits.sort(key=len)
print("Fruits sorted by length using .sort():", Fruits)
Fruits2 = sorted(Fruits, key=len)
print("Fruits sorted by length using sorted():", Fruits2)

Fruits.sort(key=str.lower)
print("Fruits sorted case-insensitively using .sort():", Fruits)
Fruits2 = sorted(Fruits, key=str.lower, reverse=True)
print("Fruits sorted case-insensitively using sorted():", Fruits2)

# using condition 
numbers = [1, -2, 3, -4, 5]
numbers.sort(key = lambda x:abs(x))
print("Numbers sorted by absolute value using .sort():", numbers)
numbers2 = sorted(numbers, key = lambda x:abs(x), reverse=True)
print("Numbers sorted by absolute value using sorted():", numbers2)
numbers3 = [ 23,45,12,67,34,89,90,11]
numbers3.sorted(key = lambda x: (x%10, x)) # sort by last digit first, then by the number itself
print("Numbers sorted by last digit using sorted():", numbers3)
'''


# 🔹 4. List Comprehension
# What is list comprehension? Syntax?
'''
# List comprehension: concise syntax to build lists
# Syntax: [expression for item in iterable if condition]

# 1) Convert a list of strings to uppercase
words = ["hello", "world", "python", "list"]
upper_words = [w.upper() for w in words]
print("Uppercase:", upper_words)

# 2) Generate a list of squares of numbers
squares = [n * n for n in range(1, 11)]
print("Squares 1..10:", squares)

# 3) Conditional list comprehension (keep only even numbers' squares)
even_squares = [n * n for n in range(1, 11) if n % 2 == 0]
print("Even squares:", even_squares)

# 4) Nested list comprehension (flatten a 2D matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
flattened = [value for row in matrix for value in row]
print("Flattened matrix:", flattened)

# 5) Nested comprehension with condition (flatten and keep odd values)
odd_values = [v for row in matrix for v in row if v % 2 == 1]
print("Odd values from matrix:", odd_values)

# Convert a list of strings to uppercase using list comprehension.
# Generate a list of squares of numbers using list comprehension.
# Use conditional list comprehension (if inside comprehension).
# Nested list comprehension (matrix flattening).

'''

# 🔹 5. Iteration & Functions with Lists
# How to iterate through both index and value using enumerate()?
'''
Name = ['Mahadeb','jayanta','Narayan','Madhurima']
for index, value in enumerate(Name):
    print(f"{value}, Index of {index}")

#without enumerate()
for i in range(len(Name)):
    print(f"{Name[i]}, Index of {i}")

'''

# How do you find the maximum, minimum, and sum of a list?
'''
Numbers = [2,3,5,7,2,6,9,2,10]
print(max(Numbers))
print(min(Numbers))
print(sum(Numbers))
print(Numbers.count(2))
Numbers.sort()
print(Numbers)
print(set(Numbers))

'''

# How to check if all elements of a list are even numbers?
'''
numbers = [4,6,8,90,12,16,18]
even_numbers = all(num % 2 == 0 for num in numbers)
print(even_numbers)
'''

# How do you filter out odd numbers from a list? (using loop/filter/comprehension).
'''
# using loop 
# numbers = [1,2,3,4,5,6,7,8,9]
# odd_numbers = []
# for item in numbers:
#     if item%2!=0:
#         odd_numbers.append(item)

# print(f"Original Numbers list:{numbers}")
# print(f"Odd number list : {odd_numbers}")

# using filter
# odd_numbers2 = list(filter(lambda x: x%2!=0,numbers))
# print(f"Original Numbers list:{numbers}")
# print(f"Odd number list : {odd_numbers2}")

# using list comprehension 
# odd_numbers3 = [odd for odd in numbers if odd%2!=0]
# print(f"Original Numbers list:{numbers}")
# print(f"Odd number list : {odd_numbers3}")

'''

# How do you apply a function to each element of a list? (map()).
'''
def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *=i
    return result

numbers = [2,3,4,5,6,7,8,9]
fact_of_all_num = list(map(factorial,numbers))
print(fact_of_all_num)

'''
# How do you reduce a list to a single value? (reduce()).
'''
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)

Key Point:
map() → transforms each element.
filter() → selects some elements.
reduce() → combines everything into a single value.
'''

# 6. Advanced List Usage
# Difference between is and == in lists?
'''
'==' → Value Equality
Checks whether two lists have the same contents (element by element).
Doesn’t care if they are stored in different memory locations.

'is' → Identity Equality
Checks whether two variables point to the same object in memory.
Even if lists have the same values, if they are two different objects, is will return False.

list1 = [1,2,3]
list2 = [1,2,3]
# Value_Equality
print(list1 == list2) # return output: True  becuase it check a value into a both list 
#Identity_Equality
print(list1 is list2) # return output: False becuase it check a value only memory address of a list 
'''

# How does shallow copy vs deep copy work for lists?
'''
list1 = [ 2,3,4,5,6,7]
shallow_copy = list1
shallow_copy.append(20)
print(f"this is shalow copy: becuase change value both but change only copied list \nOriginal List:{list1}\nCopied list:{shallow_copy}")
list2 = [ 2,3,4,5,6,7]
deep_copy = list2.copy()
deep_copy.append(25)
print(f"this is deep copy because only change deep copy list not original list,\nOriginal List:{list2}\nCopied list:{deep_copy}")

'''
# How do you create a nested list (2D list)?
'''
inner_list = []
for _ in range(1,5):
    j =[]
    for i in range(1,6):
        j.append(i)
    inner_list.append(j)

print(inner_list)
'''

# How to access elements from a nested list?
'''
nested_list = [[1,2,3,4,5],[6,7,8,9],[10,11,12,13,24,25]]
access_element = nested_list[1][2]
print(access_element)

# one way
for index,sublist in enumerate(nested_list):
    print(f"{index}:{sublist} => Length: {len(sublist)}")

# another way 
lists = [f"{index}:{sublist} => Length: {len(sublist)}" for index,sublist in enumerate(nested_list)]
for item in lists:
    print(item)
'''
    
# How do you flatten a nested list into a single list?
'''
nested_list = [[1,2,3,4,5],[6,7,8,9],[10,11,12,13,24,25]]
flatten_list = [number for sublist in nested_list for number in sublist]
print(f" Flatten list means convert  nested list into a single list: {flatten_list}")
'''

# Explain list aliasing with an example.
'''
same as shallow copy and deep copy 
'''
# 🔹 7. Interview / Tricky Questions
# What happens when you multiply a list of lists? Example: [[0]*3]*3.
'''
list1 = [[1,2,3]*2]*3
print(list1)

'''
# What is the difference between list(range(5)) and [range(5)]?
'''
print(list(range(5)))
print(list([range(5)][0]))
'''

# What happens if you try to modify a list while iterating over it?
'''
list1 = [1,2,3,4,5]
j =5
for i in range(len(list1)):
    list1[i]= j
    j +=1

print(list1)
'''

# Difference between tuple and list in Python.
'''
list is a mutable (can be change after creation) but tuple is a immutable (can not be change after creation).
List syntax: square brackets but tuple syntax is parenthesis.
List has many methods but tuple has only few methods.
List uses more memory space but tuple uses less memory.
List uses for Dynamic collection data change but Tuple uses for fixed collections so data can't change. 
'''    

# Can you use a list as a dictionary key? Why or why not?
'''
No , we can't use a list as a dictionary key becuase 
Dictionary key must be immutable and hashable but list is a mutable its content can change .
Python cannot guarantee a fixed hash value for the list → so it’s unhashable and invalid as a key.
'''
# How does Python internally store a list? (dynamic array concept).
'''
Advanced concept only 
'''
# Explain the difference between .sort() and sorted(). Which one is better?
'''
Use .sort() when you only care about sorting the current list.

Use sorted() when you care about keeping the original data safe.

data = [3, 1, 2]

# Using sort()
a = data.copy()
a.sort()
print(a)        # [1, 2, 3]
print(data)     # [3, 1, 2]  (original unchanged due to copy)

# Using sorted()
b = sorted(data)
print(b)        # [1, 2, 3]
print(data)     # [3, 1, 2]

'''

# How do you remove duplicates from a list?
'''
using set() method 
'''





# Important things in python  Zip() method 
'''
What is zip()?
zip() is a built-in function that combines multiple iterables (lists, tuples, etc.) element-wise.
It pairs the first elements together, second elements together, and so on.
Stops at the shortest iterable if they have different lengths.


Number_list1 = [1,2,3,4]
Number_list2 = [5,6,7,8]
Number_list3 = [9,10,11,12]
# print(list(zip(Number_list1,Number_list2,Number_list3)))

for a,b,c in zip(Number_list1,Number_list2,Number_list3):
    # print(a * b * c)
    print(a, "*", b, "*",c ,"=", a*b*c)

'''
