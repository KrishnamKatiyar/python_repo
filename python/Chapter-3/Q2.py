# Write a program to fill in a letter template given below with name and date.
#    letter = '''
#          Dear <|Name|>
#          You are selected!
#          <|Date|>
#    '''


letter = '''Dear <|Name|>
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Krishnam").replace("<|Date|>", "26 November 2070"))
