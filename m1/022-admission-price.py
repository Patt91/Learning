
group=[]
age=()


while True:
    age=input('insert age of visitor')
    if age == ' ':
        break
    elif 0 < int(age) <= 2:
        group.append(0)
    elif 2< int(age) <=12:
        group.append(14)
    elif 2< int(age) <=12:
        group.append(18)
    elif int(age) >65:
        group.append(18)
    else:
        group.append(23)
    
print(f'the total price is {sum(group)} $')