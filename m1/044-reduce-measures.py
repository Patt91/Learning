
y=input('insert the measure meter; tablespoons, teaspoons, cup \n')
x=int(input('insert the quantity \n'))
cup=()
teaspoons=()
teaspoons=()


if y == 'cup':
    x=x*16
elif y == 'teaspoons':
    x=x*4


while x != 0:
    cup = int(x/16)
    x=x%16
    teaspoons= int(x/4)
    x=x%4
    tablespoons= int(x/1)
    x=0

print(f'you need {cup} cup, {teaspoons} teaspoons, {tablespoons} tablespoons')