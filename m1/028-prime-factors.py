
n=int(input('insert a value >2 \n'))
if n <=2:
    print('error')

factor=2

while n != 0:
    if n % factor == 0:
        n = n // factor 
        print (factor)
    else:
        factor += 1
        