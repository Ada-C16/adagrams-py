import random


def draw_letters():
    """
    Builds and returns a list of 10 random letters
    for the user to pick from based on contents in letter_bank 
    """

    letter_bank = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1,
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
    """
    checks if all letters in word (input) are in the letter_bank
    returns True if all letters in word are in letter_bank
    returns False if all letters are not in letter_bank or
    if count of letter in word > count of letter in letter_bank
    """

    # Created copy of letter_bank to leave original letter_bank unchanged
    letter_bank_copy = letter_bank.copy()
    
    # Checks every letter in letter_bank_copy and word
    # Checks quantity of letter in letter_bank_copy and word
    # Returns value of letter: either Truthy or Falsy
    for char in letter_bank_copy:
        for char in word:
            if char not in letter_bank_copy:
                return False
            elif char in letter_bank_copy and word.count(char) > letter_bank_copy.count(char):
                return False
        return True


def score_word(word):
    """ 
    Calculates score of word based on value lists below
    and logic in conditional statements
    Returns score
    """
    # each element in list is assigned a value from 1 -7
    val_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    val_2 = ["D", "G"]
    val_3 = ["B", "C", "M", "P"]
    val_4 = ["F", "H", "V", "W", "Y"]
    val_5 = ["K"]
    val_6 = ["J", "X"]
    val_7 = ["Q", "Z"]

    # Initializes score before applying logic below
    score = 0

    # Checks len of word, if word is empty, and case of word
    # in order to determine score
    if len(word) in range(7, 11):
        score += 8
    elif word == "":
        score = 0
    elif word != word.upper():
        word = word.upper()

    # Checks each letter in word to determine value to add to score
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

    # returns word score
    return score


def get_highest_word_score(word_list):
    """ 
    Determines which word is the highest scoring by applying logic below
    Returns highest scoring word with the score in a tuple (score_tuples)
    """

    # Initialize variables
    score_tuples = []
    current_high_score = 0
    winning_word_length = 0

    # Iterate through each word
    for word in word_list:
        # check for new high score
        if score_word(word) > current_high_score:
            current_high_score = score_word(word)
            winning_word_length = len(word)
            score_tuples = ((word, score_word(word)))

        # If tied for high score
        if score_word(word) == current_high_score:
            if len(word) < winning_word_length and winning_word_length != 10:
                score_tuples = ((word, score_word(word)))
                winning_word_length = len(word)

            # Length 10 edge case
            elif len(word) == 10 and winning_word_length != 10:
                score_tuples = ((word, score_word(word)))
                winning_word_length = len(word)

    # return high score as tuple
    return score_tuples
