from random import randint
from game_data import data
from art import vs
import os

length = len(data)
random = randint(1, length)
celebs = []
celebs.append(data[random])

def guessCeleb():
  os.system('cls')
  print(f"Compare A: {celebs[-1]['name']} {celebs[-1]['description']} from {celebs[-1]['country']} ")
  print (vs)
  secondGuess = randint(1,length)
  celebs.append(data[secondGuess])
  print(f"Against B: {data[secondGuess]['name']} {data[secondGuess]['description']} from {data[secondGuess]['country']} ")
  print("choose the highest follower celebs A/B")
  return input("Guess the correct celebs having more follow: ").lower()

isCorrect=True
score=0
while isCorrect:
    response =guessCeleb()
    if response =='b':
        if celebs[-1]['follower_count'] < celebs[-2]['follower_count']:
            celebs.pop()
            print(f"YOU LOOSE and Your final score {score} ")
            isCorrect=False
        else:
            celebs.pop(0)
            score+=1
            print(f"You are right your score is {score}")
    else:
        if celebs[-1]['follower_count'] > celebs[-2]['follower_count']:
            celebs.pop(0)
            print("YOU LOOSE and your fibal score is {score} ")
            isCorrect=False
        else:
            celebs.pop()
            score+=1
            print(f"You are right your score is {score}")


      
