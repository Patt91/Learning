
list=[]
x=()
while x != 0:
    x=int(input('insert a value \n'))
    list.append(x)

list.pop(-1)
for i in list:
    print(i)