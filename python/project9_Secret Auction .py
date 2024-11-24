# replit - to clear the input in the console.
#from replit import clear
#from art import logo
#print(logo)

def find_highest_bidder(bidding_record):
   highest_bid=0
   winner=""
   for bidder in bidding_record:
      bid_amount=bidding_record[bidder]
      if bid_amount > highest_bid:
         highest_bid=bid_amount
         winner=bidder
   print(f"The winner is {winner} with a bid of ${highest_bid}")


bids={}
bidding_finished=False
while not bidding_finished:
  name=input("what is Your name: ")
  price=int(input("What is Your bid?: $"))
  bids[name]=price

  should_continue=input("Are there any other bidders? Type 'yes' or 'no'.")
  if should_continue=="no":
      bidding_finished=True
      find_highest_bidder(bids)
 # elif should_continue=="yes":
      #clear()





#My code. this time Mine is better than her(angela)  haaa! 

"""
bid={}
win=[]

print("Welcome to the secret auction program")

continued =True
while continued:
   name=input("what is Your name: ")
   waga=int(input("What is Your bid: "))
   bid[name]=waga
   win.append(waga)
   choose=input("Are there any other bidders? Type 'yes' or 'no'")
   #clear()
   if choose=="no":
      continued=False
       
#print(bid)
#print(win)

print(f"winner is {max(win)}")

"""




    