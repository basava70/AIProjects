# RockPaperSciccors game
# created on July 25

import random


def iswin(computer, human):
    if computer == human:
        return 0  # draw game
    elif (computer - human) in [-1, 2]:
        return -1  # computer wins
    else:
        return 1  # human wins


def game():
    values = ["p", "r", "s"]
    Values = ["paper", "rock", "sciccors"]
    computer = values.index(random.choice(values))  # gathering indices of the list

    human = values.index(
        input("Enter your choice as 'r' for rock, 'p' for paper and 's' for sciccors\n")
    )
    # gathering indices of the list
    # rock > sciccors, sciccors > paper, paper > rock

    win_bool = iswin(computer, human)
    match (win_bool):
        case 0:
            print("The game ended as as draw")
        case 1:
            print("You won!!", Values[human], " beats ", Values[computer])
        case -1:
            print("You lost!!", Values[computer], "beats", Values[human])


if __name__ == "__main__":
    while True:
        game()
