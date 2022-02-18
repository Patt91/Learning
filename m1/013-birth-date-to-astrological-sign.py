#this program returs the zodiac sign by entering a date

days=int(input('insert the day of your birdays\n'))
month=int(input('insert the month of your birdays\n'))

if month == 1 and days >= 20:
    print('the sign si Aquarius')
elif month == 2 and days < 18:
    print('the sign is Pisces ')

if month == 2 and days >= 19:
    print('the sign si Pisces')
elif month == 3 and days <= 21:
     print('the sign is Aries ')

if month == 3 and days >= 20:
    print('the sign si Aries')
elif month == 4 and days <= 21:
     print('the sign is Taurus ')

if month == 4 and days >= 20:
    print('the sign si Taurus')
elif month == 5 and days <= 21:
     print('the sign is Gemini ')

if month == 5 and days >= 20:
    print('the sign si Gemini')
elif month == 6 and days <= 21:
     print('the sign is Cancer ')

if month == 6 and days >= 20:
    print('the sign si Cancer')
elif month == 7 and days <= 22:
     print('the sign is Leo ')

if month == 7 and days >= 23:
    print('the sign si Leo')
elif month == 8 and days <= 22:
     print('the sign is Virgo ')

if month == 8 and days >= 23:
    print('the sign si Virgo')
elif month == 9 and days <= 22:
     print('the sign is Libra ')

if month == 9 and days >= 23:
    print('the sign si Libra')
elif month == 10 and days <= 21:
     print('the sign is Scorpio ')

if month == 11 and days >= 23:
    print('the sign si Scorpio')
elif month == 12 and days <= 21:
     print('the sign is Sagittarius ')

if month == 12 and days >= 22:
    print('the sign si Libra')
elif month == 1 and days <= 22:
     print('the sign is Capricorn ')




