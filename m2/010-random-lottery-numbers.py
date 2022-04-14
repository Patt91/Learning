import random
#this function find a 6 number
def lottery():
    win=[]
    while len(win) <= int(6):
        x=random.randint(1,49)
        if x not in win:
            win.append(x)
    print(win)

lottery()
