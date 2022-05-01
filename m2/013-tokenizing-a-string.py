
#this funciton trasform an math string in subtring

def subtrings(math):
    operators=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "(", ")", "[", "]", "{", "}"]
    token=[]
    for ope in math:
        if ope in operators:
            token.append(ope)
    return (token)

