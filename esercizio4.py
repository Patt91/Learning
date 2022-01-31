#this program converts the duration entered by the user into seconds 

day = int(input ('insert number of day  '))
hours = int(input ('insert number of hours  '))
minuts = int(input ('insert number of minutus  '))
seconds = int(input ('insert number of seconds  '))

convert= (day * 86400) + (hours * 3600) + (minuts *60) + seconds

print(f' the duration in seconds is', {convert}, 'seconds')
