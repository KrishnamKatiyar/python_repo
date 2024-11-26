name = "krishnam katiyar"

# len () function - This function returns the length of the strings.

print(len(name))  # output : 16

# String.endswith("ish") - This function tells whether the variable string ends withthe string "ish" or not. If string is "krish", it returns true for "ish" since krish ends with ish.

naam = "krish"

print(naam.endswith("ish"))  # output : True

# String.count("c") - counts the total number of occurrences of any character.

print(name.count("k"))  # output : 2
print(naam.count("i"))  # output : 1

# string.capitalize() - This function capitalize the first character of a given string.

print(name.capitalize())  # output : Krishnam katiyar


# lower() - Converts all characters in the string to lowercase.

text = "Hello, World!"
print(text.lower())  # Output: hello, world!

# upper() - Converts all characters in the string to uppercase.

text = "Hello, World!"
print(text.upper())  # Output: HELLO, WORLD!

# strip() - Removes any leading or trailing whitespace.

text = "  Hello, World!  "
print(text.strip())  # Output: Hello, World!

# split() - Splits the string into a list based on a delimiter (default is space).

text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']

# join() - Joins elements of a list into a single string with a specified separator.

fruits = ['apple', 'banana', 'cherry']
print(", ".join(fruits))  # Output: apple, banana, cherry

# replace() - Replaces a substring with another string.

text = "I like apples"
print(text.replace("apples", "bananas"))  # Output: I like bananas

# find() - Finds the first occurrence of a substring. Returns -1 if not found.

text = "Hello, World!"
print(text.find("World"))  # Output: 7

# startswith() and endswith() - Checks if the string starts or ends with a specified substring.

text = "Hello, World!"
print(text.startswith("Hello"))  # Output: True
print(text.endswith("!"))        # Output: True

# title() - Converts the first character of each word to uppercase

text = "hello, world!"
print(text.title())  # Output: Hello, World!

# isalpha() - Returns True if the string contains only alphabetic characters.

text = "HelloWorld"
print(text.isalpha())  # Output: True

# isdigit() - Returns True if the string contains only numeric characters

text = "12345"
print(text.isdigit())  # Output: True

# isalnum() - Returns True if the string contains only alphanumeric characters (letters and numbers)

text = "Hello123"
print(text.isalnum())  # Output: True



