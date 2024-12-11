'''
Q5 - Write a class Train which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.
'''
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Book train no. {self.trainNo} from {fro} to {to}.")

    def getStatus(self):
        print(f"Train no. {self.trainNo} is running successfully.")

    def getFare(self, fro, to):
        print(f"fare of train no. {self.trainNo} from {fro} to {to} is {randint(255,566)}")


train = Train(123329)
train.book("delhi", "mumbai")
train.getFare("delhi", "mumbai")
train.getStatus()