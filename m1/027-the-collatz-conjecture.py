
value =int(input('insert a value\n'))
collatz=[]
collatz.append(value)

while collatz[-1] != 1:
    if collatz[-1] %2 == 0:
        value= value / 2
        collatz.append(value)
    else:
        value= (value*3) + 1
        collatz.append(value)
print(collatz)