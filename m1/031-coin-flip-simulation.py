
import random
H=int(0)
T=int(0)
c=int()
list=[]
cont=int(0)

for i in range(1,10):
    while H < 3 and T < 3:
        flip=random.randint (0, 1)
        if flip == 1:
            T=T+1
            H=0
            list.append('T')
            c=c+1
        elif flip == 0:
            T=0
            H=H+1
            list.append('H')
            c=c+1
    print(f'{list} {c} flip')
    cont=cont+c
    H=0
    T=0
    c=0
    list=[]

print(f'the avarege is {cont/10}flip')



