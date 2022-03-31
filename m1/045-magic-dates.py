
def magic ():
    year=1901
    day=1
    month=1

    while year != 2001:
        month=1
        while month < 12:
            day=1
            while day < 31:
                if (day*month) == (year%100):
                    print(f'{day, month, year} is a magic day')
                day=day+1
            month=month+1
        year=year+1

magic()