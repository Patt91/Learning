
n_order=float(input('insert the number of items'))

def shipping(i):
    if i <= 1:
        print('the cost of shipping is 10.99 $')
    else:
        i=(i-1)*2.99
        print(f'the cost of shipping is {i+10.99} $')

shipping(n_order)
