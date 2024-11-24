import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# my code
"""
user=int(input("wt do choose? type 0 for rock,1 for paper, 2 for scissorsn: "))
if user==0:
   print(rock)
elif user==1:
   print(paper)
elif user==2:
   print(scissors)

computer=random.randint(0,2)
if user>=0 and user<=3:

   if computer==0:
      print("computer chose:\n",rock)
   elif computer==1:
      print("computer chose:\n",paper)
   else:
      print("computer chose:\n",scissors)

   if user==0 and computer==2:
      print("You win!")
   elif user==2 and computer==1:
      print("You win!")
   elif user==1 and computer==0:
      print("You win!")
   elif computer==user:
      print("it's a draw")
   else:
      print("You lose! computer win")
else:
   print("invalid No,You lose!")

"""


images=[rock,paper,scissors]
user=int(input("wt do choose? type 0 for rock,1 for paper,2 for scissorsn: "))
if user>=3 or user<0:
   print("invlid No,You lose!")
else:
  print(images[user])

  computer=random.randint(0,2)
  print("computer chose:")
  print(images[computer])
  print(f"computer chose {computer}")

  if user==0 and computer==2:
     print("You win!")
  elif computer==0 and user==2:
     print("You lose!")
  elif computer > user:
     print("You lose!")
  elif user > computer:
     print("You win")
  elif computer==user:
     print("it's a draw")




#Rule for the game 
"""
rock wins against scissors
scissors wins against paper
paper wins against rock
draw,if both the same.
"""








