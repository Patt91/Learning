
c4=261.63
d4=293.66
e4=329.63
f4=349.23
g4=392.00
a4=440.00
b4=493.88

note=str(input('insert a note and the program returns the frequency  '))

lista=['c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4']
conta=()
lista_n=[c4, d4, e4, f4, g4, a4, b4]

if note in lista:
    conta = + 1
print (lista_n[conta])

c4=261.63
lista_c=[]
x=0
r=()
while x <= 7:
    r= c4 / 2**(4-x)
    x += 1
    lista_c.append(r)
print (lista_c)

lista_f=['c0','c1','c2','c3','c4','c5','c6','c7','c8']

if note in lista_f:
    conta =+ 1
print (lista_c[conta])
