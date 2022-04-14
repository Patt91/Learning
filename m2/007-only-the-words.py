
def remuve(string):
    no_word=[',','.','!','?','-','_',';',':']
    new_string=str()
    for word in string:
        if word not in no_word:
            new_string=new_string+word
    print(new_string)
            
frase=str(input('insert a frase\n'))

remuve(frase)