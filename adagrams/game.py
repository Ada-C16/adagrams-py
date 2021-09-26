import random
import string

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

LETTER_SCORE = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K",): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10,
}


def draw_letters():
    letters = []
    while len(letters) < 10:
        random_letter = random.choice(string.ascii_uppercase)
        if letters.count(random_letter) >= LETTER_POOL[random_letter]:
            continue
        else:
            letters.append(random_letter)
    return letters


def uses_available_letters(word, letter_bank):
    for letter in word:
        if word.count(letter) > letter_bank.count(letter):
            return False
    return True


def score_word(word):
    score = 0
    for letter in word.upper():
        for key in LETTER_SCORE:
            if letter in key:
                score += LETTER_SCORE.get(key)
    if 7 <= len(word) <= 10:
        score += 8
    return score


def get_highest_word_score(word_list):
    max_score = 0
    for word in word_list:
        score = score_word(word)
        if score > max_score:
            max_score = score
            max_score_word_list = [word]
        elif score == max_score:
            max_score_word_list.append(word)

    winner = select_winner(max_score_word_list)
    return winner, max_score


def select_winner(word_list):
    min_word = word_list[0]
    for word in word_list:
        if len(word) == 10:
            return word
        elif len(word) < len(min_word):
            min_word = word
    return min_word
