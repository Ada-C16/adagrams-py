import random

def draw_letters():
    letter_bank = {'A':9, 'B':2, 'C':2, 'D': 4, 'E': 12, 'F': 2, 'G':3, 'H': 2, 'I': 9, 'J': 1, 'K':1, 'L':4, 'M': 2, 'N':6, 'O': 8, 'P':2, 'Q':1, 'R': 6, 'S': 4, 'T':6, 'U':4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z':1}
    tile_bag = []
    for k, v in letter_bank.items():
        for each_letter in range(v):
            tile_bag.append(k)

    tile_list = []
    for ten_letters in range(10):
        letter = random.choice(tile_bag)
        tile_list.append(letter)
        tile_bag.remove(letter)

    return tile_list
   

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass