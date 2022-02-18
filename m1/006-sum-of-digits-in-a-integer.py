#this program reads a four-digit integer from the user and displays the sum of its digits

number = int(input('insert a four-digit integer'))

a=number%10
number=int(number/10)
b=number%10
number=int(number/10)
c=number%10
number=int(number/10)
d=number%10
number=int(number/10)

print(a+b+c+d)


