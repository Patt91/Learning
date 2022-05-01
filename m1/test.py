
import random


values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
suits = ["s", "h", "d", "c"]
desk=[]
for value in values:
    for suit in suits:
        card=value + suit
        desk.append(card)
    card=()
print(len(desk))
print(desk)

random_desk=[]
while len(random_desk) != 52:
    card=random.choice(desk)
    if card not in random_desk:
        random_desk.append(card)
    card=()
print(random_desk)