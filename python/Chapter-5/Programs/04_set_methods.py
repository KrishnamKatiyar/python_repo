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

