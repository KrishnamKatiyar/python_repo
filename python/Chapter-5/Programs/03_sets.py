'''
A set in Python is a built-in data type that represents a collection of unique, unordered elements. 
Sets are useful for tasks involving membership testing, eliminating duplicate entries, or performing mathematical set operations like union, intersection, and difference.

Key Features of Sets :-
1. Unordered: Elements in a set do not maintain a specific order.
2. Unique: A set automatically removes duplicate entries.
3. Mutable: Sets are modifiable; you can add or remove elements.
4. Immutable Elements: Only immutable objects (e.g., numbers, strings, tuples) can be added to a set.

'''

# You can create a set using curly braces {} or the set() function.

# Using curly braces
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Using the set() function
empty_set = set()  # Creates an empty set
not_a_set = {}     # This creates an empty dictionary

'''
Adding and Removing Elements :-
-> Adding an element: Use add() to insert a single element.
-> Adding multiple elements: Use update() with an iterable.
-> Removing elements: Use remove(), discard(), or pop().
'''

my_set = {1, 2, 3}

# Add an element
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Add multiple elements
my_set.update([5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Remove an element
my_set.remove(3)  # Throws KeyError if the element doesn't exist
my_set.discard(10)  # Does not throw an error if the element doesn't exist

# Remove and return a random element
my_set.pop()


