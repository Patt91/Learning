
#This program calculates the exact amount of change due to the customer.

from decimal import DivisionImpossible


change = int(input (print('how many cents you have' )))

toonie = change / 200
change %= 200
loonie= change /100
change %= 100
quarter= change / 25
change %= 25
dine = change / 10
change %= 10
nickel = change / 5
change %= 5
pennies = change / 1
change %=1

print (f' your change in {int(toonie)} toonies, {int(loonie)} loonies, {int(quarter)} quartes, {int(dine)} dine, {int(nickel)} nickles, {int(pennies)} pennies')