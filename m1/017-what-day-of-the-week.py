
from math import floor


year=int(input('inser a year'))

day_of_the_week =((year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7)

print(day_of_the_week)

if day_of_the_week == 0:
    print ('tha day was Sunday')
elif day_of_the_week == 1:
    print ('tha day was Monday')
elif day_of_the_week == 2:
    print ('tha day was Tuesday')
elif day_of_the_week == 3:
    print ('tha day was Wednsday')
elif day_of_the_week == 4:
    print ('tha day was Thursday')
elif day_of_the_week == 5:
    print ('tha day was Suturday')
elif day_of_the_week == 6:
    print ('tha day was Sunday')
