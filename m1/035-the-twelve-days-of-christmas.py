from operator import index


first=('A partridge in a pear tree')
second=('Two turtle-doves')
third=('Three French hens')
fourth =('Four calling birds')
fifth =('Five golden rings (five golden rings)')
sixth =('Six geese a laying')
seventh = ('Seven swans a swimming')
eighth = ('Eight maids a milking')
ninth =('Nine ladies dancing')
tenth =('Ten lords a-leaping')
eleventh=('I sent 11 pipers piping')
twelfth=('12 drummers drumming')
ritor=['first','second','thirth','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
strofe=[first,second,third,fourth,fifth,sixth,seventh,eighth,ninth,tenth,eleventh,twelfth]

c=0

a=input('insert the number of verse or insert all for the all verse\n')

def play():
    global a
    global c
    if a in ritor:
        indx=ritor.index(a)
        print(strofe[indx])   
    else:
        for a in range (1,12):
            print (f'On the {ritor[c]} day of Christmas My true love sent to me {strofe[c]}')
            c=c+1

play()