# A tuple is an immutable data type in python

# ------------------------------------------------

# count() - Returns the number of times a specified value appears in the tuple.
# Syntax: tuple.count(value)

my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2))  # Output: 3


# -------------------------------------------------

# index() - Returns the index of the first occurrence of a specified value. Raises a ValueError if the value is not found.
# Syntax: tuple.index(value[, start[, stop]])

my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.index(2))  # Output: 1

# -------------------------------------------------

# len() - Returns the length of the tuple.

my_tuple = (1, 2, 3, 4)
print(len(my_tuple))  # Output: 4

# -------------------------------------------------

# max() - Returns the maximum value in the tuple (all elements must be comparable)

my_tuple = (1, 2, 3, 4)
print(max(my_tuple))  # Output: 4

# -------------------------------------------------

# min() - Returns the minimum value in the tuple

my_tuple = (1, 2, 3, 4)
print(min(my_tuple))  # Output: 1

# --------------------------------------------------

# sum() - Returns the sum of all numeric elements in the tuple

my_tuple = (1, 2, 3, 4)
print(sum(my_tuple))  # Output: 10

# --------------------------------------------------

# sorted() - Returns a sorted list of the tuple's elements (does not modify the tuple)

my_tuple = (3, 1, 4, 2)
print(sorted(my_tuple))  # Output: [1, 2, 3, 4]

# --------------------------------------------------

# any() - Returns True if any element in the tuple is truthy.

my_tuple = (0, False, 5)
print(any(my_tuple))  # Output: True

# --------------------------------------------------

# all() - Returns True if all elements in the tuple are truthy.

my_tuple = (1, 2, 3)
print(all(my_tuple))  # Output: True

# --------------------------------------------------

# tuple() - Converts an iterable (like a list) into a tuple

my_list = [1, 2, 3]
print(tuple(my_list))  # Output: (1, 2, 3)



