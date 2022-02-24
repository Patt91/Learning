
ordinal=['first','second','third','fouth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
number=['1','2','3','4','5','6','7','8','9','10','11','12']

def ord(i):
    if i in number:
        n=number.index(i)
        print(f'the ordinal namber is {ordinal[n]}')
    else:
        print('   ')

num=input('inser a number\n')

ord(num)