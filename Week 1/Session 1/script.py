# We write a comment
"""
    Multiple line comments:
    Line 1 
    Line 2
    ..
"""


# Data Types
# Primitive Types
# Number
number = 5
number_1 = 5.5

# Boolean
bool_1 = True
bool_2 = False

# String
string = "This is a string."

# Composite Types
# Lists
list_1 = [1,2,3,4,True,False,"String", [1,2,3]]
list_1[6] = "A question"
list_1.append(True)
list_1.append(False)
print(list_1)

# Tuple
tuple_1 = (1,2,3,True,"Strings")
print(tuple_1)
list_2 = list(tuple_1)
# print(list_2)
list_2.append(9001)
# print(list_2)
tuple_1 = tuple(list_2)
print(tuple_1)

# Dictionary
dictionary_1 = {
    "name": "Bob",
    "age": 25,
    "is_married": False,
    "name": "John"
}
dictionary_1["is_married"] = True
dictionary_1['last_name'] = "Johns"
print(dictionary_1['last_name'])
dict_2 = dictionary_1

dict_2['name'] = "John"
print(dictionary_1)