

def random_p ():
     import random
     n=random.randint(7,10)
     password=[]
     for p in range(n):
          password.append(chr(random.randint(33,126)))
     print("".join(password))

random_p()