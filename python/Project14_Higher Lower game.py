from art import logo,vs
from gameData import data
import  random 
# from replit import clear

def format_data(account):
	"""Format the account data into printable format."""
	account_name=account["name"]
	account_desc=account["description"]
	account_country=account["country"]
	return f"{account_name},a {account_desc},from {account_country}"
	
def check_answer(guess,a_followers,b_followers):
 """Take the user guess and follower counts and returns if they got it right."""
 if a_followers > b_followers:
 	 return guess == "a"
 else:
 	 return guess == "b"
 
 
 
print(logo)
score=0
account_b=random.choice(data)
should_continue=True
while should_continue:
   #generate a random account from the game data
   account_a=account_b
   account_b=random.choice(data) 
   while account_a==account_b:
	    account_b=random.choice(data)

   print(f"compare A:    {format_data(account_a)}")
   print(vs)
   print(f"Againist B: {format_data(account_b)}")

   #ask User for a guess
   guess=input("Who has more followers? Type 'A' or 'B':  ").lower()

   #check if the user is correct or not
   ##Get follower count of each account
  
   a_follower_count=account_a["follower_count"]
   b_follower_count=account_b["follower_count"]
   is_correct= check_answer(guess,a_follower_count,b_follower_count)
   
   #clear the screen and then print the logo
   # clear()
   #print(logo)

   #give user feedback on their guess and score keeping
   if is_correct:
     score+=1
     print(f"You are right! current score: {score}")
   else:
     should_continue=False
     print(f"Sorry,that is wrong. Final score: {score}.")





