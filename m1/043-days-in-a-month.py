#this funcion check it out the day of the month based of the year
def check (month,year):
    m_31=[1,3,5,7,8,10,12]
    m_30=[4,6,9,11]
    leap=0
    if (year % 4) == 0:
        leap=1
    if month in m_31:
        print('the month has 31 days')
    elif month == 2:
        if leap == 1:
            print ('the month has 29 days')
        else:
            print ('the month has 28 days')
    elif month in m_30:
        print('the month has 30 days')

check(12,1995)