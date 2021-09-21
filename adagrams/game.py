import random


def draw_letters():
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
    letters = []
    while len(letters) !=10:
        letter = random.choice(list(LETTER_POOL.keys()))
        if LETTER_POOL[(letter)] !=0:
            letters.append(letter)
            LETTER_POOL[(letter)] -=1
        else:
            continue
    return letters


def uses_available_letters(word, letter_bank):
    copy_letter_bank = letter_bank.copy()
    for letter in word:
        if letter in copy_letter_bank:
            copy_letter_bank.remove(letter)
        else:
            return False
    return True


def score_word(word):
    word = word.upper()
    score = 0
    SCORE_CHART = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2, 
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
    }

    for letter in word:
        score += SCORE_CHART[letter]
    if len(word) == 7 or len(word) == 8 or len(word) == 9 or len(word) == 10:
        score = score + 8

    return score


def get_highest_word_score(word_list):
    score_list = []
    for word in word_list:
        score_list.append(score_word(word))
    max_score = max(score_list)
    max_index = [i for i, x in enumerate(score_list) if x == max_score]
    if len(max_index) == 1:
        max_word = word_list[(max_index[0])]
        winner = max_word,max_score
        return winner
    else:
        max_word_1 = word_list[(max_index[0])]
        max_word_2 = word_list[(max_index[1])]
        if len(max_word_1) >=10:
            winner = max_word_1,max_score
            return winner
        elif len(max_word_2) >=10:
            winner = max_word_2,max_score
            return winner
        elif len(max_word_1)<len(max_word_2):
            winner = max_word_1,max_score
            return winner
        elif len(max_word_2)<len(max_word_1):
            winner = max_word_2,max_score
            return winner