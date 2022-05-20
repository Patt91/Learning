
message=input('insert a message')

text = {
    1:['.',',','?','!'],
    2:['A','B','C'],
    3:['D','E','F'],
    4:['G','H','I'],
    5:['J','K','L'],
    6:['M','N','O'],
    7:['P','Q','R','S'],
    8:['T','U','V'],
    9:['W','X','Y','Z'],
    0:[' ']
    }

press=""
for i in range(0,len(message)):
    for key in text:
        if message[i] in text[key]:
            digit_index= text[key].index(message[i])
            digit=key*(digit_index+1)
            press=+digit
print(f"Total key presses: {press}")
