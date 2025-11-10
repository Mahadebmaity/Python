#  Discuss About Python  Dictionary all possible Questions with answer and Additional concept

#  🧠 A. Basics and Definition
# What is a dictionary in Python?
# What is the syntax of a Python dictionary?
'''
In python, Dictionary is a Data Structure that store data as a key-value pairs.
Dictionary items(key and value pairs) are ordered, mutable and do not allow dupplicate keys. allow can only values.

Syntax:  dict_name = {
    "key1":"Value1",
    "key1":"Value1",
    .....
}

'''
# How is a dictionary different from lists, tuples, and sets?
'''
Dictionary is a different from lists , tuples and set because dictionary store data in the form of key-value pairs but 
list, tuples only store individual Element ( values only) not keys. 
and set store only unique and unordered element.

Example: 
Dictionary:
student = {
    "Name" : "Mahadeb",
    "Age": 22
}

List:
Student = ["Mahadeb",22]
tuple:
Student = ("Mahadeb",22)
set:
Student = {"Mahadeb",22}
'''
# What are dictionary keys and values?
'''
In programming, dictionaries store data in key-value pairs,
key: A key acts like an index — it must be unique and immutable (e.g., string, number, or tuple).
value: A value is the data or information associated with that key — it can be of any data type (string, list, dictionary, etc.),
       Can be duplicated: Unlike keys, multiple values within a dictionary can be identical. 


# A dictionary where names are keys and ages are values
person = {
    "name": "Alice", # "name" is the key, "Alice" is the value
    "age": 30,       # "age" is the key, 30 is the value
    "city": "New York" # "city" is the key, "New York" is the value
}

# To access a value, you use its key
print(person["name"])    # Output: Alice

# To add a new key-value pair, or to update an existing one
person["job"] = "Engineer" # "job" is a new key, "Engineer" is its value
person["age"] = 31         # Updates the value for the "age" key

# The updated dictionary now looks like this
print(person)
# Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

'''
# Can a dictionary have duplicate keys? Why or why not?
# Can dictionary values be duplicated? 
'''
No,Dictionary Can not have Duplicate keys because each key in a dictionary must be unique — if a duplicate key is assigned, the latest value will overwrite the previous one.
and immutable ( Not changable).

deeply:
Reason:
A dictionary is internally implemented using a hash table.
Each key is converted into a hash value, and only one entry per hash can exist.
Therefore, duplicate keys are not allowed, but values can be duplicated.
'''
# How to create an empty dictionary?
'''
empty_Dict = {}
print(empty_Dict,type(empty_Dict))
# output will be: {} <class 'dict'>
'''
# How to create a dictionary using the dict() constructor?
'''
Employee_Info = dict(Nama = "Mahadeb Maity",Age = 22,Address = "Manikara",IsMarried = False)
print(Employee_Info)
'''
# How is a dictionary mutable?
'''
A dictionary is mutable because its contents (key–value pairs) can be changed after creation —
meaning you can add, modify, or remove items without creating a new dictionary.

student = {"name": "Mahadeb", "age": 22}
student["age"] = 23   # Modifying existing value
print(student)
student["course"] = "MCA"   # Adding new item
print(student)
'''

# What data types can be used as dictionary keys?
'''
Dictionary keys must be immutable and hashable. 
Allowed types include: int, float, str, bool, tuple (of immutables), and frozenset. 
Mutable types like list, set, and dict cannot be used as keys.
'''
# ⚙️ B. Dictionary Creation and Initialization

# How to create a dictionary using curly braces {}?
'''
Student = { 
    "Name": "Mahadeb Maity",
    "Age": 22,
    "Course": "MCA"
}
print(Student)
'''

# How to create a dictionary using the dict() function?
'''
Student = dict(Name="Mahadeb Maity", Age = 22 , Course = "MCA")
print(Student)
'''

# How to convert a list of tuples into a dictionary?
'''
student = dict([("Name","Mahadeb"),("Age",22),("Course","MCA")])
print(student)
'''
# How to create a dictionary using fromkeys() method?
'''
# The fromkeys() method creates a dictionary with given keys and a single default value.
Student = dict.fromkeys(["Name","Age","Course"],"Unknown")
print(Student)
'''
# How to create nested dictionaries?

# How to create a dictionary using dictionary comprehension?
'''
keys = ['Name','Age','Course']
values = ['Mahadeb Maity',22,'MCA']
Student = {key:value for key,value in zip(keys,values)}
print(Student)
'''
# How to create a dictionary dynamically using user input?
'''
Student = {}
n = int(input("Enter number of Students: "))
for _ in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    Student[name] = {"Age": age, "Course": course}
print(Student)
'''

# How to merge two or more dictionaries?
'''
s1 = {"Name": "Mahadeb", "Age": 22}
s2 = {"Course": "MCA", "City": "Manikara"}
s3 = {"Roll": 20135648 , "No": 546, "Exam_Vanue" : "Kharagpur town"}
s1.update(s2) # marge two or more Dictionary 
print(f"After Marge of s2 with s1: {s1}")
s1.update(s3)
print(f"After Marge of s3 , s2 both with s1: {s1}")
'''


# 🔍 C. Accessing Dictionary Elements
# How to access dictionary values using keys?
'''
Dict1 = {"Name": "Mahadeb Maity", "Age": 22}
print(f"Name of the Student: {Dict1["Name"]}") # Accessing value into Dict1
print(f"Age of {Dict1['Name']} : {Dict1['Age']}") 
'''

# What happens if you access a non-existing key using brackets []?
'''
try:
    print(f"Access Non existing key using [] symbol : {Dict1["Address"]}")
except Exception as e:
    print(f"Key's not Exist! {e}")
finally:
    print("Execution Complete!")
'''

# What is the get() method?
'''
# Why is get() called a “safe” way to access values?
# How to access nested dictionary elements?
# How to use get() with nested dictionaries?

Answer of the both Questions :
get() is a method to access Dictionary key value pair safely without  occurs any error if key's does't exists into  given Dictionary 



there are two ways to access nested dictionary key's and value pairs 
'''
Studentinfo ={
    "Name": "Mahadeb Maity",
    "Age" : 22,
    "Education" :{
        "MP": "Dasagram S S Siksha sadan in 2020",
        "HS": "Same as MP in 2022",
        "Graduation" : "Panskura Banamali Collage in 2022-2025",
        "Masters" : "Haldia Information of Technology in 2025-2027"
    }
}
'''
#  accessing value into  nested Studentinfo  dict 
print(f"print Whole nested Dictionary  using [] :\n{Studentinfo["Education"]}") 
print(f"print Specific key value  using [] :\n{Studentinfo["Education"]["Masters"]}") 

print(f"print Whole nested Dictionary  using get() method :\n{Studentinfo.get("Education")}") 
print(f"print Specific key value  using Get() method :\n{Studentinfo.get("Education").get("Masters")}") 

'''

# How to use in operator to check if a key exists?
'''
if "Address" in Studentinfo:
    print("Address key is found!") # here else block is done 
else:
    print("key's not found!")

if "Address" not in Studentinfo:
    print("key's not found!") # here if block is done 
else:
    print("Key's found Successfully!")
'''

# How to access all keys, values, and items from a dictionary?
'''
# access all
print("print All keys from Studentinfo Dict.")
for keys in Studentinfo:
    print(keys)

print("All values from Studentinfo Dict.")
for values in Studentinfo.values():
    print(values)

for key, value in Studentinfo.items():
    print(key ,":", value)
'''

# ✏️ D. Updating and Modifying
# How to add a new key-value pair to a dictionary?
"""
Studentinfo["Address"] = "Panskura RS"
print(f"Add  new key value pairs: {Studentinfo}")
"""

# How to update an existing value in a dictionary?
'''
Studentinfo["Age"] = 23
print(f"Update age of student {Studentinfo['Name']} :Now Student Age is: {Studentinfo['Age']}")
'''

# What does the update() method do?
'''
change previous value which is change and  replace new value 
'''
# How to update multiple key-value pairs at once?
'''
# using update function
student = {"name": "Mahadeb", "age": 22, "course": "MCA"}
# Update multiple keys
student.update({"age": 23, "city": "Kolkata", "college": "XYZ University"})
print(student)
'''

# using dictionary marging operator (|=)
"""
Studentinfo |= {"Address":{"Current" : "Panskura", "Permanent": "Manikara"}}
print(f"Marge two Dict: \n{Studentinfo}")
"""
# Merging two dictionaries into a new one
"""
student = {"name": "Mahadeb", "age": 22}
update_info = {"age": 23, "city": "Kolkata"}

new_student = {**student, **update_info}
print(new_student)
"""

# How to copy a dictionary? (difference between = and copy())
'''
student = {"name": "Mahadeb", "age": 22}
Copied_Studentinfno = student
Copied_Studentinfno["Address"] = "Panskura" # update key and value pairs into Copied dict 
print(Copied_Studentinfno)
print(student) # both  will be change when change copied dict becuase I assign dict not copied 

Copied_Studentinfno2 = student.copy()
Copied_Studentinfno2["Address"] = "haldia"
print(Copied_Studentinfno2)
print(student) # not change key value pair into original dict only update copied dict 

'''


# Can we change dictionary keys? Why or why not?
'''
No, we can't change dictionary key becuase it's immutable in python . 
'''
# Can dictionary values be mutable objects like list or dict?
'''
Yes, Dictionary values be mutable objects like list 
'''

# 🗑️ E. Deleting and Clearing
# How to delete a specific key-value pair using del?
'''
Studentinfo2 ={
    "Name": "Mahadeb Maity",
    "Age" : 22,
    "Education" :{
        "MP": "Dasagram S S Siksha sadan in 2020",
        "HS": "Same as MP in 2022",
        "Graduation" : "Panskura Banamali Collage in 2022-2025",
        "Masters" : "Haldia Information of Technology in 2025-2027"
    }
}
del Studentinfo2["Education"]["MP"]
print(Studentinfo2)
'''
# What happens if you delete a non-existent key?
'''
del Studentinfo["Address"] # key Error occurs when delete non-existing key value
print(Studentinfo)
''' 
# How to remove an item using pop()?
'''
delete_item = Studentinfo.pop("Age")
print(Studentinfo)
print(f"Deleted item : {delete_item}")

Deleted_items = Studentinfo.popitem() # this is delete item from the end of the dictionary 
print(Studentinfo)
print(Deleted_items)
'''

# What is the difference between pop() and popitem()?
'''
Differ of pop() and popitem()

pop() use only specific items to delete  but both can return deleted items 
popitems() use only delete items at the end of the dictionary
'''
# How to clear all items from a dictionary?
'''
Studentinfo.clear() # this is clear all key and value pairs just return empty dict 
print(Studentinfo)
'''
# How to delete the entire dictionary?
'''
del Studentinfo
print(Studentinfo) # Output comes to error becuase dictionary was deleted using del 
'''

# 🔁 F. Looping and Iteration
# How to iterate through keys in a dictionary?
'''
for keys in Studentinfo:
    print(Studentinfo[keys]) # print All value pairs 
'''

# How to iterate through values in a dictionary?
'''
for value in Studentinfo.values():
    print(value)
'''
    
# How to iterate through both keys and values using .items()?
'''
for key , value in Studentinfo.items():
    print(key , ":" , value)
'''
    
# How to use enumerate() with a dictionary?
'''
for i,(key,value) in enumerate(Studentinfo.items()):
    print(f"{key}:{value}(Index of:{i})")
'''

# How to iterate through nested dictionaries?

# How to sort dictionary keys and values during iteration?
'''
student = {
    "Rahul" : 68,
    "Sahil" : 78,
    "naren" : 23,
    "Mahadeb" : 34,
    "Arjun" : 76
}
for key in sorted(student): # sorted order only 
    print(key, ":" , student[key])

for key in sorted(student,reverse=True): # this is reverse sorted order
    print(key , ":", student[key])
'''

# 🧮 G. Dictionary Functions and Methods
# List all built-in dictionary methods.
# Explain and show examples of:
# dict.clear()
'''
souravinfo = {
    'Name' : 'sourav',
    'roll' : 10,
    'sub' : {
        "Sub1" : "Javascript",
        "Sub2" : "React"
    },
    "Address" : "Laro"
}
# print(souravinfo)
souravinfo.clear()
print(souravinfo)
'''
# dict.copy()
# dict.fromkeys()
# dict.get()
# dict.items()
# dict.keys()
# dict.pop()
# dict.popitem()
# dict.setdefault()
# dict.update()
# dict.values()


# What is the difference between dict() and copy.deepcopy()?
'''
| Feature                  | `dict()`                                   | `copy.deepcopy()`                                   |
| ------------------------ | ------------------------------------------ | --------------------------------------------------- |
| **Purpose**              | Creates a **shallow copy** of a dictionary | Creates a **deep copy** (copies nested objects too) |
| **Affects Nested Dict?** | ❌ No                                     | ✅ Yes                                              |
| **Library**              | Built-in                                   | From `copy` module                                  |
| **Syntax**               | `new_dict = dict(old_dict)`                | `import copy; new_dict = copy.deepcopy(old_dict)`   |

import copy

d1 = {"a": 1, "b": {"x": 10}}
d2 = dict(d1)             # Shallow copy
d3 = copy.deepcopy(d1)    # Deep copy

d1["b"]["x"] = 99
print(d2["b"]["x"])   # 99 → affected
print(d3["b"]["x"])   # 10 → not affected

'''
# What does setdefault() method do?
'''
setdefault() Method

Definition:
Returns the value of a key if it exists; otherwise, inserts the key with a given default value.

Syntax:

dict.setdefault(key, default_value)
student = {'name': 'Riya', 'age': 20}
student.setdefault('marks', 90)
print(student)

'''

# 🧩 H. Advanced and Nested Dictionary
'''
# What is a nested dictionary?
# How to access elements in a nested dictionary?
# How to update or delete elements in a nested dictionary?
# How to iterate over a nested dictionary?

# A dictionary within another dictionary
# example : 
students = {
    "101": {"name": "Riya", "marks": 85},
    "102": {"name": "Amit", "marks": 92}
}
print(students["101"]["name"])  # Output: Riya
students["101"]["marks"] = 95
del students["102"]["marks"]

for roll, info in students.items():
    print(f"Roll: {roll}")
    for key, value in info.items():
        print(f"   {key}: {value}")

        

# How to flatten a nested dictionary?

def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep))
        else:
            items[new_key] = v
    return items

students = {'101': {'name': 'Riya', 'marks': 85}}
print(flatten_dict(students))

# How to convert a nested dictionary into JSON format?

import json
print(json.dumps(students, indent=2))

'''


# 💡 I. Dictionary Comprehension
# What is dictionary comprehension?
# What is the syntax of dictionary comprehension?
'''
What is Dictionary Comprehension?

A short way to create dictionaries using an expression inside {}.

syntax:
{key_expr: value_expr for item in iterable}

'''

# How to create a dictionary from two lists using comprehension?
'''
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)

'''
# How to create a dictionary from a list of tuples using comprehension?
'''
pairs = [('a', 1), ('b', 2)]
d = {k: v for k, v in pairs}

'''
# How to apply condition/filter in dictionary comprehension?
'''
d = {x: x**2 for x in range(6) if x % 2 == 0}

'''
# How to swap keys and values using dictionary comprehension?
'''
d = {'a': 1, 'b': 2}
swapped = {v: k for k, v in d.items()}

'''
# How to create a nested dictionary using comprehension?
'''
nested = {x: {y: y**2 for y in range(2)} for x in range(3)}
print(nested)

'''


# 🔄 J. Conversion and Operations
# How to convert dictionary keys/values to list, set, or tuple?
"""
d = {'a': 1, 'b': 2}
print(list(d.keys()))
print(set(d.values()))
print(tuple(d.items()))
"""
# How to convert two lists into a dictionary using zip()?
'''
keys = ['x', 'y']
vals = [10, 20]
d = dict(zip(keys, vals))

'''
# How to convert a dictionary into a list of tuples using .items()?
'''
print(list(d.items()))

'''
# How to reverse a dictionary (keys as values and values as keys)?
''''
rev = {v: k for k, v in d.items()}

'''
# How to check equality between two dictionaries?
'''
a = {'x': 1, 'y': 2}
b = {'y': 2, 'x': 1}
print(a == b)  # True

'''
# What happens if two dictionaries have the same keys but different values?
'''
a = {'x': 1, 'y': 2}
b = {'x': 5, 'y': 2}
print(a == b)  # False

'''

# 📊 K. Real-world and Program-based Questions
# Write a program to count the frequency of each word in a string using a dictionary.
# Write a program to count character occurrences using a dictionary.
# Write a program to find the key with the maximum value.
# Write a program to find the key with the minimum value.
# Write a program to sum all the values in a dictionary.
# Write a program to sort a dictionary by key.
# Write a program to sort a dictionary by value.
# Write a program to merge two dictionaries into one.
# Write a program to remove duplicate values from a dictionary.
# Write a program to create a dictionary of squares of numbers (1 to n).
# Write a program to print a multiplication table using a dictionary.
# Write a program to store and display student data (name, roll, marks) using a nested dictionary.
'''
| No | Task                    | Example                                                          |
| -- | ----------------------- | ---------------------------------------------------------------- |
| 1  | Word frequency          | `{w: text.count(w) for w in text.split()}`                       |
| 2  | Character count         | `{ch: s.count(ch) for ch in s}`                                  |
| 3  | Max value key           | `max(d, key=d.get)`                                              |
| 4  | Min value key           | `min(d, key=d.get)`                                              |
| 5  | Sum of values           | `sum(d.values())`                                                |
| 6  | Sort by key             | `dict(sorted(d.items()))`                                        |
| 7  | Sort by value           | `dict(sorted(d.items(), key=lambda x: x[1]))`                    |
| 8  | Merge                   | `{**d1, **d2}`                                                   |
| 9  | Remove duplicate values | `{k: v for k, v in d.items() if list(d.values()).count(v) == 1}` |
| 10 | Squares (1–n)           | `{x: x**2 for x in range(1, n+1)}`                               |
| 11 | Multiplication table    | `{i: i*5 for i in range(1, 11)}`                                 |
| 12 | Student data            | `{101: {'name':'Riya','roll':101,'marks':85}}`                   |

'''

# 🧠 L. Conceptual & Theory
# Why are dictionaries unordered (before Python 3.7)?
# From which Python version are dictionaries ordered?
# What is hashability, and why are dictionary keys required to be hashable?
# What is the internal implementation of a dictionary (hash table concept)?
# What is dictionary unpacking (**) and how is it used in functions?
# How is in operator used with a dictionary?
# What happens if you use a mutable object as a key?
# How is dictionary memory-efficient compared to a list of tuples?
# How are collisions handled in Python dictionaries?
# How are dictionaries used in real-world applications (e.g., JSON, database mapping)?
'''
| Concept                  | Explanation                                                                    |
| ------------------------ | ------------------------------------------------------------------------------ |
| **Unordered before 3.7** | Dictionaries used hash tables without insertion order guarantee.               |
| **Ordered from 3.7+**    | Dicts preserve insertion order (officially guaranteed).                        |
| **Hashability**          | Keys must be immutable (like string, int, tuple) so hash value doesn’t change. |
| **Internal structure**   | Implemented as a **hash table** (key → hash → index → value).                  |
| **Unpacking (`**`)**     | Expands dictionary items into function arguments or merges two dicts.          |
| **`in` operator**        | Checks only keys, not values → `'x' in d` checks if `'x'` is a key.            |
| **Mutable key issue**    | Mutable types like list cannot be hashed → error if used as key.               |
| **Memory efficiency**    | Dicts use hashing → faster lookups than lists of tuples.                       |
| **Collision handling**   | Python uses **open addressing** and **probing** to resolve hash collisions.    |
| **Real-world uses**      | JSON, database mappings, config files, data caching, API responses.            |

'''

# All possible Dictionary operations with various example using various methods and functions 
# End of Dictionary



# Just for testing purpose