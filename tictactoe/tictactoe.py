# Tictactoe using minimax from cs50 ai lecture 0 search
# Written on July 28

import copy
import random


# initial state
def initial_state():
    return [" " for _ in range(9)]


# returns whos turn is it to play
def player(board) -> str:
    if board.count("X") == board.count("O"):
        return "X"
    else:
        return "O"


# returns all possible actions
def actions(board) -> list[int]:
    return [i for i, x in enumerate(board) if x == " "]


# return the next state of the board after the action a
def result(board, action) -> list[int]:
    letter = player(board)
    new_board = copy.deepcopy(board)
    new_board[action] = letter
    return new_board


# returns the winner of the game if there is one
def winner(board):
    # check initial state
    if board.count(" ") == 9:
        return False

    current_letter = "X" if player(board) == "O" else "O"
    # checking horizontally
    for row_index in range(3):
        row = board[row_index * 3 : (row_index + 1) * 3]
        if all(current_letter == letter for letter in row):
            return row[0]

    # checking vertically
    for col_index in range(3):
        col = [board[col_index + i * 3] for i in range(3)]
        if all(current_letter == letter for letter in col):
            return col[0]

    # checking diagonally
    # first checking [0, 4, 8]
    diagonal = [board[i] for i in [0, 4, 8]]
    if all(current_letter == letter for letter in diagonal):
        return board[4]

    # second checking for [2, 4, 6]
    diagonal = [board[i] for i in [2, 4, 6]]
    if all(current_letter == letter for letter in diagonal):
        return board[4]

    return False


# returns true if the game is ending
def terminal(board) -> bool:
    # if there is a winner then return true
    if winner(board):
        return True

    # else check for empty square
    elif 0 == board.count(" "):
        return True

    # if neither game has not ended
    else:
        return False


# returns 1 if X is winning, -1 if O is winning and 0 if its a tie
def utility(board) -> int:
    # check if the game is at the end
    player = winner(board)

    # return 1 if X wins
    if player == "X":
        return 1

    # return -1 if O wins
    elif player == "O":
        return -1

    # returns 0 if its a tie
    else:
        return 0


# randomly picking a valid move without much thought
def random_choice_ai(board) -> int:
    action = random.choice(actions(board))
    return action


# using minimax algorithm to determine ai's next move
def ai_choice(board):
    # return any corner for the first move, as its statistically the best choice
    if board.count(" ") == 9:
        return 0

    # if game ended return none
    if terminal(board):
        return None

    # defining best_action to be none
    best_action = None

    # for X player, we choose max of all min results
    # as least possible negative number is -1 , we choose -2 instead of -INF
    if player(board) == "X":
        best_value = -2
        for action in actions(board):
            value = min_value(result(board, action))

            # if value is 1, we are good we can return the action
            if value == 1:
                return action

            # else we check if best_value < value
            elif best_value < value:
                best_value, best_action = value, action

    # for O player, we choose the min of all max results
    # as least possible negative number is 1 , we choose 2 instead of INF
    else:
        best_value = 2
        for action in actions(board):
            value = max_value(result(board, action))

            # if value is -1, we are good we can return the action
            if value == -1:
                return action

            # else we check if best_value < value
            elif best_value > value:
                best_value, best_action = value, action

    return best_action


# returns the maximum value for the current player
def max_value(board) -> int:
    if terminal(board):
        return utility(board)

    # set best value = -2 instead of -INF
    best_value = -2
    for action in actions(board):
        best_value = max(best_value, min_value(result(board, action)))

        # found killer move, prune other actions
        if best_value == 1:
            break
    return best_value


# returns the maximum value for the current player
def min_value(board) -> int:
    if terminal(board):
        return utility(board)
    best_value = 2
    for action in actions(board):
        best_value = min(best_value, max_value(result(board, action)))
        # found killer move, prune other actions
        if best_value == -1:
            break
    return best_value


# printing the board
def print_board(board):
    print(board[0], "|", board[1], "|", board[2], "  indices  | 0 | 1 | 2 | ")
    print(board[3], "|", board[4], "|", board[5], " --------> | 3 | 4 | 5 | ")
    print(board[6], "|", board[7], "|", board[8], "           | 6 | 7 | 8 | ")


# playing the game
def play():
    board = initial_state()
    print_board(board)
    while True:
        human = input("Choose X or O ").upper()
        if human not in ["X", "O"]:
            print("Not a valid input, try again")
        else:
            break

        # set computer mark
    computer = "X" if human == "O" else "O"

    while not terminal(board):
        # choose players move
        if player(board) == human:
            while True:
                action = int(input("Enter your choice "))
                if action not in actions(board):
                    print("Not a valid input, try again")
                else:
                    break
            board = result(board, action)
            print_board(board)
            print("Player put", human, "at", action)

        else:
            # choose computer's move
            # action = random_choice_ai(board)
            action = ai_choice(board)
            board = result(board, action)
            print_board(board)
            print("Computer put", computer, "at", action)
    if winner(board):
        print(winner(board), "wins!!")
    else:
        print("Game is a tie")


if __name__ == "__main__":
    play()
