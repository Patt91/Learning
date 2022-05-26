
from random import random

import numpy


bingo={}
add=[]

for i in range(1,16):
    add.append(i)
bingo['B']=add
add=[]

for i in range(16,31):
    add.append(i)
bingo['I']=add
add=[]

for i in range(31,45):
    add.append(i)
bingo['N']=add
add=[]

for i in range(45,61):
    add.append(i)
bingo['G']=add
add=[]

for i in range(61,76):
    add.append(i)
bingo['O']=add

def card():
    lst_Bingo=[]
    for k in bingo:
        x=bingo[k]
        y=numpy.random.choice(x)
        lst_Bingo.append(y)
    print(lst_Bingo)

card()