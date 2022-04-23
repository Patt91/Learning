

from cmath import phase
from http.client import parse_headers


x=input('insert a sentence for a translation in Latinpig\n')
vowels = "aeiou"
consonant = "bcdfghjklmnpqrstvwxyz"
phrase=x.split(' ')
phrase_final=[]
useful=[]

i=0
for word in phrase:
    if word[0] in vowels:
        add=word+'way'
        phrase_final.append(add)
    else:
        useful=[]
        add=()
        for word in word:
            useful.append(word)
        while i <= len(word):
            if useful[0] in consonant:
                add=useful[0]
                useful.append(add)
                useful.pop(0)
            i=i+1
        for z in useful:
            phrase_final.append(z)
        
    phrase_final.append(' ')
             
print("".join(phrase_final))