
#this function eliminate the duplicate in a string
def check(string):
    check_list=[]
    new_string=[]
    for i in string:
        if i not in check_list:
            new_string.append(i)
            check_list.append(i)
    print(new_string)


value=[]
x=str()
while x != ' ':
    x=input('insert a sting, when you are done insert blank line \n')
    value.append(x)
value.pop(-1)

check(value)