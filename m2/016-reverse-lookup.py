

my_dict ={"John":1, "Michael":2, "Shawn":3}

#this function find the key associed with the value
def reverseLookup(val):
    for key, value in my_dict.items():
        if val == value:
            return key
        
    print('there is not this key')

print(reverseLookup(2))