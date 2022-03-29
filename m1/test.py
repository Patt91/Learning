
x='12cd'

def hexadecimal(x):
    esa=[]
    nx=[]
    indice=0
    while indice < len(x):
        nx.append((x[indice]))
        indice=indice +1
    for i in nx:
        if i == 'A' or i == 'a':
            esa.append(10)
        elif i == 'B' or i== 'b':
            esa.append(11)
        elif i == 'C' or i == 'c':
            esa.append(12)
        elif i == 'D' or i == 'd':
            esa.append(13)
        elif i == 'E' or i == 'e':
            esa.append(14)
        elif i == 'F' or i == 'f':
            esa.append(15)
        else:
            esa.append(int(i))
    esa.reverse()
    indice=0
    c=int()
    nesa=[]
    for i in esa:
        c = i * 16**indice
        nesa.append(c)
        indice=indice+1    
    r=sum(nesa)
    print(r)

hexadecimal(x)
