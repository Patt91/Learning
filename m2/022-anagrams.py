
#this program controll if tow words are anagrams or not

x=str(input('insert a word'))
y=str(input('insert a word'))

dx={}
dy={}

for w in x:
    if w not in dx:
        dx[w] = w
    else:
        dx[w] = w,w

for s in y:
    if s not in dy:
        dy[s] = s
    else:
        dy[s] = s,s

if dx == dy:
    print('the words are anagrams')
else:
    print('the words are not anagrams')


