# Escape sequences in Python are special characters used to represent certain whitespace characters, formatting, or special instructions within strings. 
# They are denoted by a backslash (\) followed by another character.


#   ------------------------------------------------------------------------------------------------------------------------
#       Escape Sequence	            Description	                                 Example Output
#   ------------------------------------------------------------------------------------------------------------------------
#           \'	                     Single quote	                              'Hello'
#           \"	                     Double quote	                              "Hello"
#           \\	                     Backslash	                                     \
#           \n	                     New line	                                   New line
#           \t	                     Horizontal tab	                               Tab space
#           \r	                     Carriage return	                        Moves cursor to the start of the line
#           \b	                     Backspace	                                Removes previous character
#           \f	                     Form feed	                                New page in some contexts
#           \v	                     Vertical tab	                            Vertical spacing
#           \0	                     Null character	                               Null
#           \ooo	                 Octal value of a character	                Corresponding character
#           \xhh	                 Hexadecimal value of a character	        Corresponding character
#   -------------------------------------------------------------------------------------------------------------------------


# Using various escape sequences
example = "Hello,\nWelcome to Python programming!\nLet\'s learn about escape sequences.\n\t- Use \\n for a new line.\n\t- Use \\t for tabs."
print(example)


sen = "He is a \"boy\""
print(sen)

sen2 = "\\ is used for escape sequence characters"
print(sen2)