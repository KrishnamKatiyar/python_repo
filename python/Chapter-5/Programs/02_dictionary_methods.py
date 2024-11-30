'''
common dictionary methods

        Method	                 Description
---------------------------------------------------------------------------
    dict.keys()	            Returns all the keys in the dictionary
    dict.values()	        Returns all the values in the dictionary
    dict.items()	        Returns key-value pairs as tuples
    dict.update(other)	    Updates the dictionary with another dictionary
    dict.pop(key)	        Removes the key and returns its value
    dict.clear()	        Removes all items from the dictionary
---------------------------------------------------------------------------
'''


my_dict = dict(name="Krishnam", age=25, city="Delhi")

# Add or update a key-value pair
my_dict["age"] = 26  # Updates the value for 'age'
my_dict["gender"] = "Male"  # Adds a new key-value pair

# Remove a key-value pair
my_dict.pop("city")  # Removes the key 'city'


my_dict.update({"age" : 23, "email" : "krishnamkatiyar@gmail.com"}) # it will update age and email


print(my_dict.get("name2"))  # returns "none" if key doesn't exists
print(my_dict["name2"]) # returns error if key doesn't exist

