import numpy as np

#this function find proper divisor of a positive integer and find if the the sum of proper divisor make the original number
def divisor(number):
    div=[]
    for i in range(1,number):
        if (number % i ) == 0:
            div.append(i)
    print(div)
    my_array=np.array(div)
    perfect=sum(my_array)
    if perfect == number:
        print('the number is special number')
    else:
        print('the number isn t the perfect number')


divisor(28)
