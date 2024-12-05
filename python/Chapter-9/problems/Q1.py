# Q1 - Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

with open("./problems/poems.txt") as f:
    poem = f.read()
    if("twinkle" or "Twinkle" in poem):
        print("Word twinkle is present in the poem")
    else:
        print("Word twinkle not is present in the poem")