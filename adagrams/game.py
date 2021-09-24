import random

def draw_letters():

    letter_bank = {
    "A" : 9,
    "B" : 2,
    "C" : 2,
    "D" : 4,
    "E" : 12,
    "F" : 2,
    "G" : 3,
    "H" : 2,
    "I" : 9,
    "J" : 1,
    "K" : 1,
    "L" : 4,
    "M" : 2,
    "N" : 6,
    "O" : 8,
    "P" : 2,
    "Q" : 1,
    "R" : 6,
    "S" : 4,
    "T" : 6,
    "U" : 4,
    "V" : 2,
    "W" : 2,
    "X" : 1,
    "Y" : 2,
    "Z" : 1,
    }
    # Initialize variables
    letter_bank_keys = letter_bank.keys()
    letter_bank_copy = letter_bank.copy()
    letters = []
    hand_size = 0

    # Hand draw logic, including incrementer and non-zero value check
    while hand_size < 10:
        letter = random.choice(list(letter_bank_keys))
        if letter_bank_copy[letter] > 0:
            letters.append(letter)
            letter_bank_copy[letter] -= 1
            hand_size += 1

    return letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for char in letter_bank_copy:
        for char in word:
            if char not in letter_bank_copy:
                return False
            elif char in letter_bank_copy and word.count(char) > letter_bank_copy.count(char):
                return False
        return True


def score_word(word):
    val_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    val_2 = ["D", "G"]
    val_3 = ["B", "C", "M", "P"]
    val_4 = ["F", "H", "V", "W", "Y"]
    val_5 = ["K"]
    val_6 = ["J", "X"]
    val_7 = ["Q", "Z"]


    score = 0
    if len(word) in range(7,11):
        score += 8
    elif word == "":
        score = 0
    elif word != word.upper():
        word = word.upper()
    for char in word:
        if char in val_1:
            score += 1
        elif char in val_2:
            score += 2
        elif char in val_3:
            score += 3
        elif char in val_4:
            score += 4
        elif char in val_5:
            score += 5
        elif char in val_6:
            score += 8
        elif char in val_7:
            score += 10

    return score
        

def get_highest_word_score(word_list):
    score_tuples = ()
    # Initialize variables
    # Iterate through each word
    # Check for new high score
    # If tied for high score
    # Length 10 edge case
    #return high score as tuple 
    return score_tuples