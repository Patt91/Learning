
value=[1,5,2]

numbers={
    1:'one', 2:'two',3:'three',4:'four',
    5:'five', 6:'six', 7:'seven', 8:'eight',
    9:'nine', 10:'ten',11:'eleven',12:'tweve',
    13:'thirteen', 14:'fourteen',15:'fifteen',
    16:'sixteen',17:'seventeen',18:'eighteen',
    19:'ninteen'
}

dozens={
    2:'twenty', 3:'thirty', 4:'fouty', 5:'fifty',
    6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'

}

write=[]
nums=()

if len(value) == 3:
    write.append(numbers[value[0]])
    write.append('houndred')
    value.pop(0)

if value[0]>1:
    write.append(dozens[value[0]])
    value.pop(0)
    write.append(numbers[value[0]])
else:
    nums=sum(value)
    nums+=10
    write.append(numbers[nums])


print((write))