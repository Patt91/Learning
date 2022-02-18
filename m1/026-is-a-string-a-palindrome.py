
string=str(input('insert a word'))
revers=''.join(reversed(string))

if string == revers:
    print('the word is palindrome')
else:
    print('the word isn t palindrome')



