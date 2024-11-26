friends = ["Apple", "Banana", "Mango", 3, 6.774, "Ravi", "Potato"]

print(friends)

friends.append("Bob")
print(friends)

friends.extend(["adam","eve"])
print(friends)

lst = [1,2,3]

lst.extend([5,"steve"])
print(lst)

lst.insert(1,99)  # first argument is index where we want to put the value and second argument is value
print(lst)

lst.remove("steve")
print(lst)


lst.sort()
print(lst)

lst.reverse()
print(lst)

lst.index(99)
print(lst)

lst.count(5)
print(lst)

lst.pop()
print(lst)

lst.clear()
print(lst)















#------------------------------------------------------------------------------------------------------------------------
# Method          	                Description	                                                Example
#------------------------------------------------------------------------------------------------------------------------
# append(x)           	        Adds an element x to the end of the list.	                    lst.append(10)
# extend(iterable)    	        Extends the list by appending elements from another 
#                               iterable (e.g., list, tuple).	                                lst.extend([1, 2, 3])
# insert(i, x)	                Inserts an element x at index i.	                            lst.insert(2, 20)
# remove(x)	                    Removes the first occurrence of element x in the list.	        lst.remove(10)
# pop([i])	                    Removes and returns the element at index i. 
#                               Defaults to the last element if i is not provided.	            lst.pop(1)
# clear()	                    Removes all elements from the list.	                            lst.clear()
# index(x, start, end)	        Returns the index of the first occurrence of x. 
#                               Can specify a range with start and end.	                        lst.index(10, 0, 5)
# count(x)	                    Returns the number of occurrences of element x.	                lst.count(3)
# sort(key=None,reverse=False)	Sorts the list in ascending order (default). 
#                               Use reverse=True for descending order.	                        lst.sort(reverse=True)
# reverse()	                    Reverses the elements of the list in place.	                    lst.reverse()
# copy()	                    Returns a shallow copy of the list.	                            new_list = lst.copy()
#------------------------------------------------------------------------------------------------------------------------

