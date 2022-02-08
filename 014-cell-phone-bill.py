#this program calculate the bill of phone according to consumption

from turtle import back


add_min=int(input('what is the number of minutes used?\n'))
add_mes=int(input('what is the number of message used?\n'))

base=15
extra_min=0.25
extra_mes=0.15
tax=0.05
t_911=0.44
n_min=float()
n_mes=float()
total=(base + n_min +n_mes + tax)
cost= float(total + (total * 0.05))

print(f'the base charge is {(base):12}  $')
if (add_min - 50) >= 0:
    n_min = (add_min - 50)
    n_min = (n_min * extra_min)
    print(f'the cost of addictiona min is {round(n_min,2)}$')
if (add_mes - 50) >= 0:
    n_mes = (add_mes - 50)
    n_mes = (n_mes * extra_mes)
    print(f'the cost of addictiona min is {round(n_mes,2)}$')

print(f'the tax 911 is {(tax):19}$')
print(f'the total is {(round(cost,2)):20}$')
