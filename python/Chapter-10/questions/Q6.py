'''
Q6 - Can you change the self-parameter inside a class to something else (say
"harry"). Try changing self to "slf" or "harry" and see the effects.
'''

from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Book train no. {slf.trainNo} from {fro} to {to}.")

    def getStatus(slf):
        print(f"Train no. {slf.trainNo} is running successfully.")

    def getFare(slf, fro, to):
        print(f"fare of train no. {slf.trainNo} from {fro} to {to} is {randint(255,566)}")


train = Train(123329)
train.book("delhi", "mumbai")
train.getFare("delhi", "mumbai")
train.getStatus()