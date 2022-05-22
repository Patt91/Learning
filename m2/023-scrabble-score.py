
words=input('insert a words fot calcularte the point')

sum_of_point=[]
point={
    1:['A','E','I','L','N','O','R','S','T','U'],
    2:['D','G'],
    3:['B','C','M','P'],
    4:['F','H','V','W','Y'],
    5:['K'],
    8:['J','X'],
    10:['Q','Z'],
    }

key_list=list(point.keys())
value_list=list(point.values())

for val in value_list:
    for v in val:
        for w in words:
            if w == v:
                sum_of_point.append(key_list[value_list.index(val)])

print(F'the point associate of the word is {sum(sum_of_point)}')