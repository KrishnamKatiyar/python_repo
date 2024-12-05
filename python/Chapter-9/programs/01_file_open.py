f = open("text.txt")
data = f.read()
print(data)
f.close()












'''
The random-access memory is volatile, and all its contents are lost once a program
terminates in order to persist the data forever, we use files.

A file is data stored in a storage device, A python program can talk to the file by reading
content from it and writing content it.
File operations in Python allow you to read from and write to files, enabling data storage and retrieval
'''

'''
Opening Files
The open() function is used to open files.
syntax:-
file_object = open(file_name, mode)


-----------------------------------------------------------------------------
Mode	          Description
-----------------------------------------------------------------------------
'w'	          Write. Creates a new file or overwrites if it exists.
'r'	          Read (default mode). File must exist.
'x'	          Create. Fails if the file already exists.
'a'	          Append. Creates a new file or appends to an existing file.
'b'	          Binary mode. Used with other modes (e.g., 'rb', 'wb').
't'	          Text mode (default). Used with other modes (e.g., 'rt', 'wt').
'+'	          Read and write (e.g., 'r+', 'w+').
------------------------------------------------------------------------------

Reading Files:-

1. Reading the Entire File

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


2. Reading Line by Line

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Strip removes trailing newline characters


3. Reading Specific Number of Characters

with open("example.txt", "r") as file:
    content = file.read(10)  # Reads the first 10 characters
    print(content)


4. Reading All Lines as a List

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # Returns a list of lines



Writing to Files:-

1. Overwriting a File

with open("example.txt", "w") as file:
    file.write("This is a new line.")


2. Appending to a File

with open("example.txt", "a") as file:
    file.write("\nThis line is appended.")


3. Writing Multiple Lines

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)



Working with Binary Files:-
Binary mode is used for non-text files like images, videos, etc.


Writing Binary Data-

with open("example.bin", "wb") as file:
    file.write(b"This is binary data.")


Reading Binary Data-

with open("example.bin", "rb") as file:
    content = file.read()
    print(content)



File Operations:-
Checking if a File Exists

Use the os module:

import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")


Renaming a File -            os.rename("old_name.txt", "new_name.txt")

Deleting a File -            os.remove("example.txt")

Creating a Directory -       os.mkdir("new_directory")

Deleting a Directory -       os.rmdir("new_directory")



File Pointers:-
The file pointer keeps track of where to read or write in the file.


Use seek() to move the pointer-

file.seek(0)  # Move to the beginning of the file


Use tell() to find the current pointer position-

position = file.tell()
print(f"Current position: {position}")



Closing Files:-
Always close a file after use to free resources.

Use close():

file = open("example.txt", "r")
# Perform operations
file.close()


Prefer with statements to automatically close files:

with open("example.txt", "r") as file:
    content = file.read()
# File is automatically closed here




Error Handling with Files:-
Handle potential errors using try and except:

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")


Example: Combining Reading and Writing

# Copy contents from one file to another
with open("source.txt", "r") as source, open("destination.txt", "w") as destination:
    for line in source:
        destination.write(line)




Summary:-
-> Use open() to work with files.
-> Modes control whether you're reading, writing, or appending.
-> Binary mode is for non-text files.
-> Use the with statement for safe and efficient file handling.
-> Manage errors gracefully with try-except.


'''


