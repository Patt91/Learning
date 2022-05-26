

user_input = 'a'

scrabble_score = {
                1:["a", "e", "i", "l", "n", "o", "r", "s", "t", "u"], 
                2:["d", "g"],
                3:["b", "c", "m", "p"],
                4:["f", "h", "v", "w", "y"],
                5:["k"],
                8:["j", "x"],
                10:["q", "z"]
                }

scores = []

values_list = list(scrabble_score.values())
keys_list = list(scrabble_score.keys())

for val in values_list:
    for v in val:
        for l in user_input:
            if l == v:
                scores.append(keys_list[values_list.index(val)])

print("This word has " + str(sum(scores)) + " scrubble points.")