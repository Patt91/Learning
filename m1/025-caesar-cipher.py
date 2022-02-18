
from operator import ne
from re import S


string=input('insert a text')
cript=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b',' ',' ',' ']
new=[]
den=','
for i in string:
    a=cript.index(i)
    b=a+2
    c=cript[b]
    new.append(c)
print (*new)
        

