
x="3:00"
y="205:00"

y=y.split(':')
x=x.split(':')
x1=int(x[0])
x2=int(x[1])
y1=int(y[0])
y2=int(y[1])

somma=y1+y2
giorni=int(somma/24)
ore=((somma/24)-giorni)*24
ore=int(ore)
minuti=(((somma/24)-giorni)*24-ore)*60
minuti=int(minuti)

oracorretta=x*ore
if oracorretta>=24:
    giorni


print(giorni)
print(ore)
print(minuti)
print(y,y1,y2,giorni,ore)