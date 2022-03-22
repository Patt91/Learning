
from re import A

y=int(input('insert 10 if number is decimal or 16 if number is hesadecimal'))
x=input('insert a number')

def hex2int (x):
    rest=[]
    while x != 0:
        rest.append(x%16)
        x=int(x/16)
    for index, value in enumerate(rest):
        if value == 10:
            rest[index] = 'A'
        elif value == 11:
            rest[index] = 'B'
        elif value == 12:
            rest[index] = 'C'
        elif value == 13:
            rest[index] = 'D'
        elif value == 14:
            rest[index] = 'E'
        elif value== 15:
            rest[index] = 'F' 
    rest.reverse()     
    print("".join(map(str,rest)))

def hexadecimal(x):
    esa=[]
    nx=[]
    indice=0
    while indice < len(x):
        nx.append((x[indice]))
        indice=indice +1
    for i in nx:
        if i == 'A' or i == 'a':
            esa.append(10)
        elif i == 'B' or i== 'b':
            esa.append(11)
        elif i == 'C' or i == 'c':
            esa.append(12)
        elif i == 'D' or i == 'd':
            esa.append(13)
        elif i == 'E' or i == 'e':
            esa.append(14)
        elif i == 'F' or i == 'f':
            esa.append(15)
        else:
            esa.append(int(i))
    esa.reverse()
    indice=0
    c=int()
    nesa=[]
    for i in esa:
        c = i * 16**indice
        nesa.append(c)
        indice=indice+1    
    r=sum(nesa)
    print(r)

if y==10:
    x=int(x)
    hex2int(x)    
else:
    hexadecimal(x)