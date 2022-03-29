x=12
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

hex2int(x)