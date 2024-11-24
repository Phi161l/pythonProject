from random import randint

EASY_lEVEL_TURNS=10  #Global variables.
HARD_lEVEL_TURNS=5

def set_difficulty():
  level=input("Choose a difficulty.Type 'easy' or 'hard:  ")
  if level=="easy":
     return EASY_lEVEL_TURNS
  elif level=="hard":
     return HARD_lEVEL_TURNS

def check_answer(guess,answer,turns):
  """ checks answer against guessa and return the No of turns remaining"""
  if guess > answer:
     print("Too high")
     return turns-1
  elif guess < answer:
     print("Too Low")
     return turns-1
  else:
     print(f"You got it!The answer was {answer}.")

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  answer=randint(1,100)
  #print(answer)
  turns=set_difficulty()

  guess=0
  while guess != answer:
    print(f"You have {turns} attempts remaining.")
    guess=int(input("make a guess: "))
    turns=check_answer(guess,answer,turns)
    if turns==0:
       print("You've run out of guesss,You lose.")
       return   #it stops the function
    elif guess != answer:
       print("Guess again")

game()













#my:
"""
def play(difficulty,n):
  choose=0
  if difficulty=="hard":
     choose=5
  elif difficulty=="easy":
     choose=10

  
  for i in range(choose):
     u=int(input("Make a guess:"))
     choose-=1
     if u>n:
       print("Too high")
       print("guess again")
       a=False
       print(f"You have {choose} attempts remaining")       
     elif u<n:
       print("Too low")
       print("guess again")
       print(f"You have {choose} attempts remaining")      
     else:
       print("U got it")
       break
  


import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty=input("Chosse a difficulty.Type 'easy' or 'hard'\n")
answer=random.randint(1,100)
#print(answer)
play(difficulty,answer)

"""










