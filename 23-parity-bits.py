c=[]
while True:
    string=(input('insert a 8 string sequence '))
    if len(string) == 8:
        c.append(string)
    elif string == ' ':
        break
    else:
        print('Error is not a 8 bit sequence')


for i in c:
    number = i.count('1')
    if number % 2 == 0:
        print(f"{i} for even parity, parity bit should be 0")
    else:
        print(f"{i} for even parity, parity bit should be 1")
