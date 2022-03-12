import random

n=random.randint(7,10)

pas=[]

for i in range(n):
     pas.append(chr(random.randint(33,126)))


print("".join(pas))

    

