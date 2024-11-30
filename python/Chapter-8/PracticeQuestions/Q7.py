# Q7 - Write a python function to remove a given word from a list ad strip it at the same time.

def rem(list,word):
    newList = []
    for item in list:
        if not(item == word):
            newList.append(item.strip(word))
    return newList


l = ["Adam", "Eve", "Bob", "Harry"]

print(rem(l,"am"))