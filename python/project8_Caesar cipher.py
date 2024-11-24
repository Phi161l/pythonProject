alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a',
 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k',
 'l', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#The short line of code with good userexperiance.

def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
           shift_amount*=-1      # the shift become minus.
    for char in start_text:
       if char in alphabet:
          position=alphabet.index(char) 
          new_position=position+shift_amount
          end_text+=alphabet[new_position]
       else:
        end_text +=char
        
    print(f"The {cipher_direction}d text is {end_text}")

#from art import logo
#print(logo)

should_continue=True
while should_continue:
  direction = input("Type 'encode' to encrypt,or type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift % 26  #getting it back within the range of  0 to 25.

  caesar(text,shift,direction)

  result=input("Type yes if U wanna ho again.otherwise no.\n")
  if result=='no':
     should_continue=False
     print("Goodbye")








#the long but with simple logic

"""
def encrypt(plain_text,shift_amount):
   cipher_text=""
   for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        cipher_text+=alphabet[new_position]
   print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text,shift_amount):
   plain_text=""
   for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        plain_text+=alphabet[new_position]
   print(f"The decoded text is {plain_text}")


#from  art import logo
#print(logo)
direction = input("Type 'encode' to encrypt,or type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#shift=shift % 26

if direction=="encode":
   encrypt(plain_text=text,shift_amount=shift)
elif direction=="decode":
   decrypt(cipher_text=text,shift_amount=shift)
"""






# my code
"""
choose=input("encrypt or decrypt:\n")

if choose=="encrypt":
   def encrypt(t,s):
       output_Str=""
       for i in text:
         shift_No=( (ord(i) - ord('a') +s) % 26) + ord('a')
         #print(shift_No)
         shifted_char=chr(shift_No)
         output_Str=output_Str+shifted_char
       print(f"The encoded text is {output_Str}")
    
   text=input("Enter a text:\n").lower()
   shift=int(input("Enter No of shift:\n"))

   encrypt(text,shift)


if choose=="decrypt":
    def decrypt(t,s):
       output_Str=""
       for i in text:
         shift_No=((ord(i) - 97 - s) % 26) + 97
         #print(shift_No)
         shifted_char=chr(shift_No)
         output_Str=output_Str+shifted_char
       print(f"The encoded text is {output_Str}")

    text=input("Enter a text:\n").lower()
    shift=int(input("Enter No of shift:\n"))
    
    decrypt(text,shift)

"""





#converting characters to unicode and vice versa 
"""
s='a'
n=65
print(ord(s))
print(chr(n))
"""

    