
#this function prints a user-supplied string defined by a defined space in the center of the screen
def center (string,width):
    list=[]
    if len(string) <= width:
        print(string)
    for i in range (width):
        list.append(' ')
    list.append(string)
    for i in range (width):
        list.append(' ')
    print("".join(list))


x=input('insert a string\n')
y=int(input('insert a width of the window\n'))
center(x,y)