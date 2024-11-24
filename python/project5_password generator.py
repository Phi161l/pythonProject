import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
letter=int(input("How many letters would you like in your password?\n")) 
number=int(input(f"How many numbers would you like?\n"))
symbol=int(input(f"How many symbols would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easy_password=""
for i in range(letter):      
   easy_password+=random.choice(letters) 
#print(ran_letter)
for i in range(number):      
   easy_password+=random.choice(numbers) 
#print(ran_No)
for i in range(symbol):      
   easy_password+=random.choice(symbols) 
#print(ran_symbol)

print(f"relatively easy password is: {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&

password_list=[]
for i in range(letter):      
   password_list+=random.choice(letters) 
#print(ran_letter)
for i in range(number):      
   password_list+=random.choice(numbers) 
#print(ran_No)
for i in range(symbol):      
   password_list+=random.choice(symbols) 
#print(ran_symbol)

random.shuffle(password_list)

hard_password=""
for char in password_list:
    hard_password+=char
print(f"hard password {hard_password}: ")





# my code,the hard password is generated from the 
#character which is all are in easy_password.
#but the above code is not. it is from directly
#genereated from the letters list.

"""
ran_letter="" 
for i in range(letter):      
   ran_letter+=random.choice(letters) 
ran_No="" 
for i in range(number):      
   ran_No+=random.choice(numbers) 
ran_symbol="" 
for i in range(symbol):      
   ran_symbol+=random.choice(symbols) 

print("\n")
easy_pass=ran_letter+ran_No+ran_symbol
print("relatively easy password: " + easy_pass)

list=[]
for i in range(letter+number+symbol):
   char=easy_pass[i]
   list.append(char)
#print(list)    

hard_pass=""
for i in range(letter+number+symbol):
   hard_pass+=random.choice(list)
print("hard password is: " + hard_pass)


"""


# ""(empty string)->is like idditive identity to strings or characters.
#ran_letter=random.choice(letters)  #Yasebkut 









