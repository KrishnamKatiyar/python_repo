# Q5 - Label the program written in problem 4 with comments.

import os

# Specify the directory path (change '.' to any specific path)
directory_path = '.'

# List all entries in the directory
contents = os.listdir(directory_path)

# Print the contents of the specified directory
print("Contents of the directory:", contents)