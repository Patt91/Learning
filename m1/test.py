
my_dict ={"John":1, "Michael":2, "Shawn":3}
def get_key(val):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "There is no such Key"
   
print(get_key(1))
print(get_key(2))
