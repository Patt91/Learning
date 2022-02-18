# this program reading the number of loaves of day old bread being purchased from the user. 
# Then show the regular price for the bread, the discount because it is a day old, and the total price

n_bread=int(input('how many old bread did you buy?'))
price=3.69
disc=60
total=(n_bread*price)*0.6
arr=(round(total,2))

print (f'The price of bread is {(n_bread*price):10} $')
print (f'the discount is {(disc):16}','%')
print (f'the total cost is {arr:14} $')