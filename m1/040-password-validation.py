
#this function check it out if the password is strong enough
def check (x):
    from tabnanny import check
    num=str(any(chr.isdigit() for chr in x))
    upper=str(any(chr.isupper() for chr in x))
    lower=str(any(chr.islower() for chr in x))
    if num == 'True' and lower == 'True' and upper == 'True':
        print('the password is secure')
    else:
        print('choose another password')

check(x=(input('insert your password\n')))