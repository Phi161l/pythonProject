import random
#from  replit  import clear
#import hangman_words

from hangman_art import logo
print(logo)

#word_list=["ardvark","baboon","camel"]

from hangman_words import word_list
chosen_word=random.choice(word_list)
print(chosen_word)

display=[]
for i in range(len(chosen_word)):
   display.append("_") #or we can say:display+="_"
#print(display)

lives=6
end_game=True
while end_game:
  guess=input("Guess a letter: ").lower()
  #clear()
  
  if guess in display:
  	print(f"U've already guessed {guess}")
  
  
  
  for i in range(len(chosen_word)):
     if chosen_word[i]==guess:
        display[i]=guess    
    
    
  if guess not in chosen_word:
      print(f"U guessd {guess},that is't in the word . You lose a life")
      lives-=1
      if lives==0:
         end_game=False
         print("You lose!")   
               
  for i in display:
    	print(i,end="")
    	
  from hangman_art import stages
  print(stages[lives])

  if '_' not in display:
     end_game=False
     print("You won!")

  



"""
for i in display:
  print(i,end="  ")
"""









"""
s="beekeeper"

b=True
for j in range(len(s)):
  sI=input()
  for  i in range(len(s)):     
     if s[i]==sI:
        print(sI,end="")
        b=False
     else:
        print('_',end="")
 
        
#n=0                 
if b:
  print("\ndraw[n]")
  #n=n+1
else:
  print("\ndraw")
        
"""




