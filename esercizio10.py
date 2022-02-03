# this program returns the number of the day in the month

month=str(input('pls insert the name of the month'))

a=['janury', 'march', 'may', 'july','august','october','dicember']
b=['april','june','sectember','november']

if month in a:
    print('the month has 31 days')
elif month in b:
    print ('the month has 30 days')
else:
    print ('the month could have 28 or 29 days')