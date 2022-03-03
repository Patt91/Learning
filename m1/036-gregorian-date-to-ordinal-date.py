
import datetime
from time import strftime

year=int(input('inset a year\n'))
month=int(input('insert a month\n'))
day=int(input('insert a day\n'))


def giorno():
    x=datetime.datetime(year,month,day)
    print(x.strftime('%a'))

giorno()