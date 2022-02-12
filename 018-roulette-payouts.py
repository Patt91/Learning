import random

x=()
num=[0]
cont=int()
for i in range(36):
    cont = cont + 1
    num.append(cont)
num.insert(0,'00')

x=random.choice(num)
red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black=set(num)-set(red)
black.remove(0)

print(f'the number is {x}')
if x == 0 or x== 00:
    print(f'pay {x}')
else:
    if x in black:
        print(f'the number is black')
    elif x in red:
        print(f'the number is red')

    if int(x%2) == 0:
        print(f'the number di odd')
    else:
        print(f'the number is Even')

    if x <= 18:
        print(f'pay 1 to 18')
    else:
        print(f'pay 19 to 36')