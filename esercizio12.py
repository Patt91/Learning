#this program returns the color of the square according to the position inserted in the chessboard

letters=str(input('insert a letter position in the chessboard \n'))
number=float(input('insert a number position in the chessboard \n'))

p=()
d=()
if number % 2 == 0:
    p =+ 1
else:
    d =+ 1

lista=['a','c','e','g']

if letters in lista:
    if p == 1:
        print ('the square is whaite')
    else:
        print ('the square in black')
else:
    if p == 1:
        print ('the square is black')
    else:
        print ('the square in white')