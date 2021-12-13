complementary_move = {
        "R": "P",
        "P": "S",
        "S": "R",
    }
string = "PRSPRPP"

for y in "RPS":
    points = 0
    for letter in string:
        if y == complementary_move[letter]:
            points+=2
        elif y == letter:
            points+=1
    print(points)
