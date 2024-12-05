'''
Q2 - The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file 'Hi-score.txt' which is either blank or contains the
previous Hi-score. You need to write a program to update the Hi-score whenever the
game() function breaks the Hi-score.
'''

import random

def game():
    print("You are playing the game.....")
    score = random.randint(1,62)

    with open("./problems/Hi-score.txt") as f:   # fetch the hi-score
        hiScore = f.read()
        if(hiScore != ""):
            hiScore = int(hiScore)  # highscore stored in file was in str type; so we have convert it in int so that we can compare it with new score
        else:
            hiScore = 0

    print(f"Your score is {score}")
    if(score>hiScore):
        with open("./problems/Hi-score.txt","w") as f:    # write hi-score to the file
            f.write(str(score))

    return score


game()
