
x=input('insert a string\n')
y=int(input('insert a width of the window\n'))
lista=[]
lenx=len(x)
width=int(y/2)

if lenx <= y:
    print(x)

for i in range (width):
    lista.append(' ')

lista.append(x)

for i in range (width):
    lista.append(' ')


print("".join(lista))