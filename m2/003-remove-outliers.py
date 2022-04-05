lista=int(input('insert the number of element'))
n=int(input('insert a number'))
list=[]

for i in range (1,lista):
    x=input('insert a value')
    list.append(x)

print(list)

for i in range(0,n):
    list.pop(0)
list.reverse()
for i in range(0,n):
    list.pop(0)

print(list)