import random
import os
from secrets import choice

class Hangman:
    wrongAttempt = 0  
    def __init__(self) -> None:
        self.wrongAttempt = 0

    def screen_clear(self):
        # for mac and linux(here, os.name is 'posix')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # for windows platfrom
            _ = os.system('cls')

    def drawHangman(self):
        #this will draw hangman
        if(self.wrongAttempt == 1):
            print("+-----+")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
        elif (self.wrongAttempt == 2):
            print("+----+")
            print("O    |")
            print("     |")
            print("     |")
            print("     |")
        elif (self.wrongAttempt == 3):
            print("  +----+")
            print("  O    |")
            print("__|__  |")
            print("  |    |")
            print("       |")
        elif (self.wrongAttempt == 4):
            print("  +----+")
            print("  O    |")
            print("__|__  |")
            print("  |    |")
            print(" /     |")
            print("       |")
        elif (self.wrongAttempt == 5):
            print("  +----+")
            print("  O    |")
            print("__|__  |")
            print("  |    |")
            print(" / \   |")
            print("       |")

    # this function will load a dynamic word from your personal dictionary
    def loadWordFromCustomDictionary(self):
        words = []
        with open('dictionary.txt') as f:
            for line in f:
                words.append(line.strip())
        return random.choice(words)

    # this function is used to evaluate wordGuess code upon entering each character
    def wordGuess (self, input_letter, previous_guess, word):
        dashes = False
        if(input_letter in word):
            previous_guess.append(input_letter)
            for i, v in enumerate(word):
                if(v in previous_guess):
                    pass
                else:
            #       print("_", end=" ")
                    dashes = True
            if not dashes:
                # it means game over -  you won!
                return 1    
        else: 
            ## print("Wrong guess")
           self.wrongAttempt = self.wrongAttempt + 1
           return 0
        # 2 means this function is executed without finding a wrongAttempt           
        return 2

    # this function is used just for display
    def correcGuess(self, previous_guess, word):
        for i, v in enumerate(word):
            if(v in previous_guess):
                print(v, end =" ")
            else:
                print("_", end=" ")

    # from this function the game start
    def startGame(self):
        self.wrongAttempt = 0 
        # this is the guess word
        word = self.loadWordFromCustomDictionary() 
        #print(word)
        self.screen_clear()
        print("Guess my word?")
        print("Note: you can guess the whole word once before you are hung")

        for i, v in enumerate(word):
            print("_", end =" ")
        
        previous_guess = []
        alphet = True
        attempt = 0
        wholeWordAttempt = 0
        while(alphet):
            attempt = attempt + 1
            input_letter = input(f"\r\n\nWhat is your guess of a letter (total attempts: {attempt})?\r\n")
            if(len(input_letter) == 1):
                response = self.wordGuess (input_letter, previous_guess, word)
                self.screen_clear()
                self.drawHangman()
                print("")
                self.correcGuess(previous_guess, word)
                if(response == 1):
                    print(" \n Congrats you won!")
                    break
                elif(response == 2):
                    continue
                else:
                    if(self.wrongAttempt >= 5):
                        print("the word was ", word)
                        break

            elif (wholeWordAttempt == 0): # this condition will execute if user try the whole word
                wholeWordAttempt = 1
                if(input_letter == word):
                    print(" \n Congrats you won!")
                    break
            else:
                print("You have consumed this option")            

# calling object of main Hungman class           
hangman = Hangman()
choice=True
while(choice==True):
    hangman.startGame()
    input_letter = input(f"\r\n\ndo you want to try again?(y)")
    if(input_letter == 'y'):
        choice= True
    else:
        choice= False    
