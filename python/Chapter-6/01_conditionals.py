age = int(input("Enter your age : "))

if(age>=18):
    print("you are above the age of consent")
    print("good for you")

else:
    print("you are below the age of consent")

print("end of program")





'''
syntax - 'value_if_true' if 'condition' else 'value_if_false'
-> condition: The condition to evaluate.
-> value_if_true: The value or expression returned if the condition evaluates to True.
-> value_if_false: The value or expression returned if the condition evaluates to False.

'''


x = 5
result = "Positive" if x > 0 else "Non-positive"
print(result)  # Output: Positive


x = 0
result = "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(result)  # Output: Zero


# Both 'value_if_true' and 'value_if_false' can involve function calls or complex expressions.
def check_number(x):
    return "Even" if x % 2 == 0 else "Odd"

print(check_number(10))  # Output: Even
print(check_number(7))   # Output: Odd
