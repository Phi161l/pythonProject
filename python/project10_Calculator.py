#from replit import clear

def add(n1,n2):
   return n1+n2
def substract(n1,n2):
   return n1-n2
def multiply(n1,n2):
   return n1*n2
def divide(n1,n2):
   return n1/n2

operations={
'+':add,
'-':substract,
'*':multiply,
'/':divide
}

def calculator():
  n1=float(input("What is the first number?: "))
  for symbol in operations:
     print(symbol)

  should_continue=True
  while should_continue:
    operation_symbol=input("pick an operation: ")
    n2=float(input("What is the next number?: "))

    calculate=operations[operation_symbol]
    answer=calculate(n1,n2)
    print(f"{n1} {operation_symbol} {n2}={answer}")

    choose=input("type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")
    if choose=='y':
       n1=answer
    else:
       should_continue=False
       #clear()
       calculator()


calculator()








#My trial it is working
"""
while True:
  n1=float(input("1st No: "))
  operations=['+','-','*','/']

  for i in operations:
      print(i)

  a=True
  while a:
  

    sign=input("pick operation: ")
    n2=float(input("2nd No: "))

    if sign=='+':
       sum=n1+n2
       print(f"{n1}+{n2}={sum}")
    elif sign=='-':
       sum=n1-n2
       print(f"{n1}-{n2}={sum}")
    elif sign=='*':
       sum=n1*n2
       print(f"{n1}*{n2}={sum}")
    elif sign=='/':
       sum=n1/n2
       print(f"{n1}/{n2}={sum}")
    else:
       print("invalid sign")
    
    choose=input("y or n: ")
    if choose=='n':
       a=False
    elif choose=='y':
       n1=sum
"""
    