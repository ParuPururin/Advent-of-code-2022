# 1 represent Rock, 2 Paper and 3 Scissors.
player = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

oponent = {
    "A": 1,
    "B": 2,
    "C": 3
}

outcome = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

score = 0
score_part2 = 0

def resolve_match(player_opt, oponent_opt):
    score = 0
    if player_opt == oponent_opt:
        score = 3
    elif player_opt == (oponent_opt % 3) + 1:   
        score = 6

    return score


def match_outcome(oponent_opt, result):
    hand = 0

    if result == "Y":
        hand = oponent_opt
    elif result == "X":
        if oponent_opt == 1:
            hand = 3
        else:
            hand = oponent_opt - 1
    elif result == "Z":
        if oponent_opt == 3:
            hand = 1
        else:
            hand = oponent_opt + 1

    return hand


with open("input.txt") as file:
    line = file.readline().rstrip()
    while line:
        oponent_hand, player_hand = line.split()
        line = file.readline().rstrip()

        score += player[player_hand]
        score += resolve_match(player[player_hand], oponent[oponent_hand])

        score_part2 += outcome[player_hand]
        score_part2 += match_outcome(oponent[oponent_hand], player_hand)

print(score)
print(score_part2)

