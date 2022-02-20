import random
n=()
l=[]
cont=int()


for i in range (1,100):
    n=random.randint(0,100)
    l.append(n)
    maxv=max(l)
    if n >= maxv:
        cont = cont +1
        print(f'{n}< == update')
    else:
        print(n)
    


print(f'the maximum value was {maxv}')
print(f'the maximum value was update {cont} time')
