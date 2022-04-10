
def misuration (misure,quantity):
    cup=()
    teaspoons=()
    teaspoons=()
    if misure == 'cup':
        quantity=quantity*16
    elif misure == 'teaspoons':
        quantity=quantity*4
    while quantity != 0:
        cup = int(quantity/16)
        quantity=quantity%16
        teaspoons= int(quantity/4)
        quantity=quantity%4
        tablespoons= int(quantity/1)
        quantity=0
    print(f'you need {cup} cup, {teaspoons} teaspoons, {tablespoons} tablespoons')

misuration('cup',16)