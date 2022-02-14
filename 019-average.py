
list=[]
v=int(1)

while v > 0:
    v=int(input('insert a value'))
    list.append(v)
    if list[0] ==0:
        print ('Error')
    
n=len(list)
s=sum(list)

print(F'the averange is {float(s / n)}')