# --------todos of project -----------
# 1. generate number
# 2. create 2 variable easy and hard
# 3. write function to tackle problem
#----------------------------------------
import random
from art import logo

NUMBER = random.randint(1,100)

#----------------function starts-------------------------------
def guess_number(chance):
    while chance>0:
        guessed_number = int(input("Guess the number: "))
        if guessed_number > NUMBER:
            print("Too high\nGuess again")
        elif guessed_number<NUMBER:
            print("Too low\nGuess again")
        else:
            print("Well done! correct guess.")
            break
        chance=chance-1
        print(f"you have {chance} guess remaining")
    if chance==0:
        print(f"You should guess{NUMBER}")
#------------function end here -------------------------


print(logo)
print("Welcome to the number guessing game")
print("I have number between 1 and 100 you have to guess the correct number")
toughness = input("Enter the label 'easy' or 'hard' ").lower()

if toughness=='hard':
    print("You have only 5 chance to guess the number")
    guess_number(5)
else:
    print("You have 10 chance to gues the number:")
    guess_number(10)