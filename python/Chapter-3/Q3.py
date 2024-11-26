# Write a program to detect double space in a string.

sentence = "Krishnam is a good boy"
print(sentence.find("  "))  # it will give -1 bcz there aren't any double spaces.

sentence_2 = "Krishnam is a  good boy"
print(sentence_2.find("  "))  # output : 13    bcz double spaces occur at index 13.
