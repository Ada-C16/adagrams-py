import random


def draw_letters():
    pool_dict = {
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
    pool_list = []
    for letter, freq in pool_dict.items():
        pool_list.extend(letter * freq)

    hand = []
    for i in range(10):
        letter = random.choice(pool_list)
        while hand.count(letter) == pool_dict[letter]:
            letter = random.choice(pool_list)
        hand.append(letter)

    return hand


def uses_available_letters(word, letter_bank):
    temp_bank = letter_bank.copy()
    for letter in word:
        if letter not in temp_bank:
            return False
        else:
            temp_bank.remove(letter)
    return True


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass
