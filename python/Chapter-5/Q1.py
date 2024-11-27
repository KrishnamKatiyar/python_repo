# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

dictionary = {
    "jao" : "go",
    "dibba" : "box",
    "basta" : "bag",
    "kursi" : "chair",
    "rassi" : "rope",
    "sheesha" : "mirror",
    "panni" : "polythin",
    "darwaza" : "door",
    "khidki" : "window",
    "madad" : "help"
}

word = input(f"Enter the hindi word you want to know meaning of from {dictionary.keys()} : ")

print(f"Meaning of this word in english is {dictionary[word]}")