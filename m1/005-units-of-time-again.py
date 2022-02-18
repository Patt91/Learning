#this program convert a numbers of second input by the user in a specific fortmat D'HH'MM'SS

sec = int( input('insert numbers of seconds  '))

dd =+ int(sec/86400)
sec = (sec - (dd*86400))

HH =+ int(sec/3600)
sec = (sec - (HH*3600))

MM =+ int( sec / 60)
sec = (sec - (MM*60))

SS =+ sec

print (f' the data is {dd}:{HH}:{MM}:{SS}')