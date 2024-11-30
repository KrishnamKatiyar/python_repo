# 1. Union (| or union())- Combines elements from both sets, eliminating duplicates.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}
print(set1.union(set2))

# 2. Intersection (& or intersection()) - Finds common elements in both sets.

print(set1 & set2)  # Output: {3}
print(set1.intersection(set2))


# 3. Difference (- or difference()) - Finds elements in the first set that are not in the second.

print(set1 - set2)  # Output: {1, 2}
print(set1.difference(set2))


# 4. Symmetric Difference (^ or symmetric_difference()) - Finds elements in either set but not in both.

print(set1 ^ set2)  # Output: {1, 2, 4, 5}
print(set1.symmetric_difference(set2))


# Membership Testing :- You can use in and not in to test membership in a set.

my_set = {1, 2, 3}
print(2 in my_set)     # Output: True
print(4 not in my_set) # Output: True


'''
Other Set Methods
1. isdisjoint(): Checks if two sets have no elements in common.
2. issubset(): Checks if one set is a subset of another.
3. issuperset(): Checks if one set is a superset of another.
'''

set1 = {1, 2}
set2 = {1, 2, 3}

print(set1.issubset(set2))  # Output: True
print(set2.issuperset(set1))  # Output: True
print(set1.isdisjoint({4, 5}))  # Output: True


# Frozensets - A frozenset is an immutable version of a set. Once created, its elements cannot be modified.

frozen = frozenset([1, 2, 3])
print(frozen)  # Output: frozenset({1, 2, 3})


# Use Cases-
# 1. Removing duplicates from a list:

my_list = [1, 2, 2, 3]
unique = list(set(my_list))
print(unique)  # Output: [1, 2, 3]

# 2. Membership testing with high efficiency.
# 3. Mathematical operations on sets (e.g., union, intersection).

