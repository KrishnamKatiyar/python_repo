'''
A dictionary in Python is a built-in data structure that stores data as key-value pairs. 
It is highly versatile, allowing fast access, insertion, and modification of data.

You can create a dictionary using curly braces {} or the dict() function.
'''

marks = {
    "ravi" : 34,
    "puneet" : 22,
    "bob" : 47,
    "henry" : 41
}

print(marks , type(marks))

print(marks["bob"])


# Using curly braces
my_dict = {"name": "Krishnam", "age": 25, "city": "Delhi"}

print(my_dict)

# Using dict() function
my_dict2 = dict(name="Krishnam", age=25, city="Delhi")

print(my_dict2)


# You can create dictionaries dynamically using a comprehension.

# Example: Squaring numbers
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}



# Dictionaries can contain other dictionaries as values.

nested_dict = {
    "student1": {"name": "Krishnam", "age": 25},
    "student2": {"name": "Rohan", "age": 24},
}

print(nested_dict["student1"]["name"])  # Output: Krishnam



'''
Key Features of a Dictionary :-

1. Unordered: Dictionaries are unordered collections. From Python 3.7+, dictionaries maintain insertion order, but this is not guaranteed in older versions.
2. Mutable: The contents of a dictionary can be changed (i.e., it's mutable).
3. Key-Value Pairs: Each element in a dictionary is a key-value pair -> key: value.
4. Keys are Unique: No two keys in a dictionary can be the same.
5. Key Constraints:
        Keys must be immutable (e.g., strings, numbers, or tuples containing immutable elements).
        Keys cannot be mutable types like lists or other dictionaries.
6. Values: Values can be of any data type and can be duplicated.
'''

