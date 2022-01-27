
#This program is used to calculate the refund following the recycling of bottles in the container


n_bottles = int(input ('how many bottles do you have? '))

minsize = int(input('How many of these are smaller or equal to a liter? '))
maxsize = int(n_bottles - minsize)

minsize = minsize*0.1
maxsize = maxsize*0.25

refund = minsize + maxsize
    

print('your refound is ', refund,'$')