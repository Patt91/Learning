#this program reads the string by the string by the user and returs if is vowel or consonant

letters=str(input('input a letters  '))

vowel=['a','e','i','o','u']

if letters in vowel:
    print ('the letter is vowel')
elif letters == 'y':
        print('sometimes y is a vowel, and sometimes y is a consonant')
else:
    print('the letter is consonant')