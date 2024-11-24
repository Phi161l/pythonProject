from question_model import tiyaqe
from data import question_data

question_bank = []
for ques in question_data:
    text = ques["text"]
    answ = ques["answer"]
    obj = tiyaqe(text, answ)
    question_bank.append(obj)



