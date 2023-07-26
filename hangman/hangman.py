# Hangman game; using the words file from
# https://www.randomlists.com/data/words.json
# created on July 26, 2023
# This code is inspired from Kylie Ying's youtube channel

from words import words  # list of all words for the computer to use
import random
import string


# Since, we have - and spaces in the words
# lets make sure the word is valid and only has alphabets
def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


# defining the actual game
def hangman():
    word = get_valid_word(words)
    alphabets = set(string.ascii_uppercase)  # list of all alphabets
    # print("choosen word = ", word)
    guessed_letters = set()  # all the letters we guessed at any given time
    word_letters = set(word)  # letters in the word

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(
            "You have ",
            lives,
            " lives. Already chosen letters: ",
            " ".join(guessed_letters),
        )

        # print the word in ad-s- style
        current_word = [letter if letter in guessed_letters else "-" for letter in word]
        print("Current word is : ", " ".join(current_word))
        # get the user input
        user_input = input("Choose a letter ").upper()
        while user_input not in alphabets:
            print("Input is not an alphabet, please enter again ")
            user_input = input("Choose a letter ").upper()
        if user_input not in guessed_letters:
            guessed_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives = lives - 1
                print(user_input, " is not in the word, try again")

        else:
            print("You have already guessed that letter, try again")

    if lives == 0:
        print("Sorry!! you couldn't guess in time, the word is ", word)
    else:
        print("Congrats!! you guessed the word ", word)


if __name__ == "__main__":
    hangman()
