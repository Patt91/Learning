
#this function find proper divisor of a positive integer
def divisor(number):
    div=[]
    for i in range(1,number):
        if (number % i ) == 0:
            div.append(i)
    print(div)

divisor(34)