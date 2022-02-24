
a=float(input('what is the total of km?'))

def costo(i):
    basefee=float(4)
    fee=float(0.25)
    cost=float(i*fee)+basefee
    print(f'the cost is {cost}')

costo(a)