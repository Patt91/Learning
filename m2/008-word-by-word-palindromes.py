import numpy as np

def controll (string):
    y=str()
    for word in string:
        no_word=[',','.','!','?','-','_',';',':']
        if word not in no_word:
            y=y+word
    y=y.split()
    revers=list(reversed(y))
    y=np.array(y)
    revers=np.array(revers)
    check=str(np.array_equal(y,revers))

    if check == 'True':
        print('the frase is palindromes')
    else:
        print('the frase isn t palindromes')

phrase=str(input('insert a frase to controll if is a palidomes, the frase must be written in lowercase\n'))
controll (phrase)
