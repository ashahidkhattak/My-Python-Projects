from random import *

class NumberGuess:

    def __init__(self):
        self.LOWER = 1
        self.HIGHER = 20
    def start(self):
        attempt = 1
        number = randrange(self.LOWER, self.HIGHER)
        #print(number)
        while True:
            userNumber = int(input(f"Guess a number from {self.LOWER} to {self.HIGHER} ? "))
            if(userNumber == number):
                print(f"Wow you are a pro! your guess was correct in your {attempt} attempt")
                break
            elif userNumber < number:
                 print("Your number is smaller than the random number")
            else:
                 print("Your number is greater than the random number")
            attempt = attempt + 1
ng = NumberGuess()
ng.start()