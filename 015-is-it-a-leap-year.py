#this programs returns if the year insered from the user is leap year 

year=int(input('insert a year \n'))

bis=float(year/400) - int(year/400)
print(bis)

if int(bis) != 0:
    print ('this is a leap year')
else:
    print('this isn t a leap year')