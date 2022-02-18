# this program reads a date from the user and computes its immediate successor

data=(input('inset a date in this format XXXX-XX-XX\n'))

data=data.split('-')
print (data)

anno=int(data[0])
mese=int(data[1])
giorno=int(data[2])

mesi30=[4, 6, 9, 11]
mesi31=[1,3,5,7,8,10,12]

if mese in mesi30:
    if giorno >= 30:
        giorno = 1 
        if mese >= 12:
            mese=1
            anno+=1
        else:
            giorno+=1
            mese+=1
    else:
        giorno += 1
elif mese in mesi31:
    if giorno >= 31:
        giorno = 1 
        if mese >= 12:
            mese=1
            anno+=1
        else:
            giorno+=1
            mese+=1
    else:
        giorno += 1
elif mese == 2:
    if giorno >= 29:
        giorno = 1 
        if mese >= 12:
            mese=1
            anno+=1
        else:
            giorno+=1
            mese+=1
    else:
        giorno += 1


print (f'{anno}-{mese}-{giorno}')
