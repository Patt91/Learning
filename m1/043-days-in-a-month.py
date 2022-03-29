
anno=int(input('insert the year as XXXX \n'))
mese=int(input('insent the number of the month as integer \n'))
bisestile=0

m_31=[1,3,5,7,8,10,12]
m_30=[4,6,9,11]


if (anno % 4) == 0:
    bisestile=1

if mese in m_31:
    print('the month has 31 days')
elif mese == 2:
    if bisestile == 1:
        print ('the month has 29 days')
    else:
        print ('the month has 28 days')
elif mese in m_30:
    print('the month has 30 days')