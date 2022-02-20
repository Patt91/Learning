
number=int(input('insert a interger numbers \n'))
binary=[]


while number != 0:
    if (number % 2) == 0:
        binary.append(0)
        number =int(number / 2)
    else:
        binary.append(1)
        number =int(number / 2)

binary.reverse()
print(binary)
