
def create_desk():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    suits = ["s", "h", "d", "c"]
    desk=[]
    for value in values:
        for suit in suits:
            card=value + suit
            desk.append(card)
        card=()
    return desk

def shuffle():
    import random
    random_desk=[]
    while len(random_desk) != 52:
        card=random.choice(desk)
        if card not in random_desk:
            random_desk.append(card)
        card=()
    return(random_desk)

desk=create_desk()
randm_desk=shuffle()

print(desk, randm_desk)