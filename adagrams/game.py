import random

# Wave 1


def draw_letters():
    """
    Uses dict to create a list of the letter pool.
    Shuffles list and returns slice of first 10 items. 
    """
    LETTER_POOL = {
        'A': 9,
        'B': 2,
        'C': 2,
        'D': 4,
        'E': 12,
        'F': 2,
        'G': 3,
        'H': 2,
        'I': 9,
        'J': 1,
        'K': 1,
        'L': 4,
        'M': 2,
        'N': 6,
        'O': 8,
        'P': 2,
        'Q': 1,
        'R': 6,
        'S': 4,
        'T': 6,
        'U': 4,
        'V': 2,
        'W': 2,
        'X': 1,
        'Y': 2,
        'Z': 1
    }

    letter_list = []
    for letter in LETTER_POOL:
        counter = 0
        while counter < LETTER_POOL[letter]:
            letter_list.append(letter)
            counter += 1

    random.shuffle(letter_list)

    return letter_list[0:10]

# Wave 2


def uses_available_letters(word, letter_bank):
    """
    Makes copy of letter bank list.
    Checks to see if all letters in the words are in the letter bank.
    """

    letter_bank_copy = []
    for item in letter_bank:
        letter_bank_copy.append(item)

    for char in word:
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False

    return True

# Wave 3


def score_word(word):
    """
    Iterates through all letters in word, adds corresponding value to sum.
    Adds 8 at the end if length of word greater than 6.
    """

    score_chart = {
        "A": 1, "E": 1, "I": 1, "O": 1,
        "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    word = word.upper()
    score = 0
    for letter in word:
        score += score_chart[letter]

    if len(word) > 6:
        score += 8

    return score

# Wave 4


def get_highest_word_score(word_list):
    """
    Iterates through word list and calculates each score.
    Checks score, length and returns winning word and score.
    """
    word_result = ""
    score_count = 0
    for given_word in word_list:
        each_word_score = score_word(given_word)
        if each_word_score > score_count:
            score_count = each_word_score
            word_result = given_word
        elif each_word_score == score_count:
            if len(given_word) != len(word_result) and len(given_word) == 10:
                word_result = given_word
            elif len(given_word) < len(word_result) and len(word_result) != 10:
                word_result = given_word

    return [word_result, score_count]
