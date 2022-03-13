
from tabnanny import check


x=(input('insert your password\n'))


num=str(any(chr.isdigit() for chr in x))
upper=str(any(chr.isupper() for chr in x))
lower=str(any(chr.islower() for chr in x))

if num == 'True' and lower == 'True' and upper == 'True':
    print('the password is secure')
else:
    print('choose another password')

