print("welcome to the tip calculator")

bill=float(input(("wt was the total bill? $")))
tip=int(input("wt %tip u liketogive? 10,12or15?"))
ppl=int(input("hw many ppl to split the bill? "))

t=tip/100*bill
bill_ppl=(bill+t)/ppl

final=round(bill_ppl,2)
final="{:.2f}".format(bill_ppl)
print(f"each person pay ${final}")



