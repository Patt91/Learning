
#this function simulate the launch of two dice, and show the number of result, the probability and the expected by probability theory
def lauch():
    import random
    result=[]
    for i in range(0,1000):
        x=random.randint(2,12)
        result.append(x)

    c2=int()
    c3=int()
    c4=int()
    c5=int()
    c6=int()
    c7=int()
    c8=int()
    c9=int()
    c10=int()
    c11=int()
    c12=int()

    for element in result:
        if element == 2:
            c2=c2 + 1
        elif element == 3:
            c3=c3+1
        elif element == 4:
            c4=c4+1
        elif element == 5:
            c5=c5+1
        elif element == 6:
            c6=c6+1
        elif element == 7:
            c7=c7+1
        elif element == 8:
            c8=c8+1
        elif element == 9:
            c9=c9+1
        elif element == 10:
            c10=c10+1
        elif element == 11:
            c11=c11+1
        elif element == 12:
            c12=c12+1
    print(f'the number of time that the lunch produced 2 is {c2}, the probability in {c2/1000}, the expected by probability theory is 2,78 %')
    print(f'the number of time that the lunch produced 2 is {c3}, the probability in {c3/1000}, the expected by probability theory is 5,56 %')
    print(f'the number of time that the lunch produced 2 is {c4}, the probability in {c4/1000}, the expected by probability theory is 8,33 %')
    print(f'the number of time that the lunch produced 2 is {c5}, the probability in {c5/1000}, the expected by probability theory is 11,11 %')
    print(f'the number of time that the lunch produced 2 is {c6}, the probability in {c6/1000}, the expected by probability theory is 13,89 %')
    print(f'the number of time that the lunch produced 2 is {c7}, the probability in {c7/1000}, the expected by probability theory is 16,67 %')
    print(f'the number of time that the lunch produced 2 is {c8}, the probability in {c8/1000}, the expected by probability theory is 13,89 %')
    print(f'the number of time that the lunch produced 2 is {c9}, the probability in {c9/1000}, the expected by probability theory is 11,11 %')
    print(f'the number of time that the lunch produced 2 is {c10}, the probability in {c10/1000}, the expected by probability theory is 8,33 %')
    print(f'the number of time that the lunch produced 2 is {c11}, the probability in {c11/1000}, the expected by probability theory is 5,56 %')
    print(f'the number of time that the lunch produced 2 is {c12}, the probability in {c12/1000}, the expected by probability theory is 2,78 %')

lauch()