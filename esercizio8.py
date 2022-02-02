#this program implements the conversion from human years to dog years

dog=int(input('how old is your dog?'))

if dog < 0:
    print('the age is wrog, are you sure?')

age = ((dog-2)*4)+21

if dog <= 2:
    print(f'the age of dog is {dog*10.5}')
else:
    print (f'the age of dog is {age}')