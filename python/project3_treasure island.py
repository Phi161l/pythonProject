print("welcome to treasure island")
print("Ur mission is to find the treasure")

s1=input("Left or right:").lower()
if s1=="left":
   s2=input("swim or wait: ").lower()
   if s2=="wait": 
      s3=input("which door red,blue or yellow :")
      s3.lower()
      if s3=="red" or s3=="blue":
         print("game over")
      elif s3=="yellow":
         print("you win!")
      else:
         print("game over")
   else:
      print("game over")
else:
   print("game over")