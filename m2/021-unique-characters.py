
#this excercise count the unique letters in a string 

words=input('insert a phase')
unique_letters={}

for w in words:
    if w not in unique_letters:
        unique_letters[w]=w

print(len(unique_letters.keys()))