import random

def dictionary_to_list(dict):
    letter_list = []
    for key, value in dict.items():
        for i in range(value): 
            letter_list.append(key)
    
    return letter_list

def draw_letters():
    letter_pool = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
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

    possible_letters = dictionary_to_list(letter_pool)

    player_hand = random.sample(possible_letters, 10)
    return player_hand

def uses_available_letters(word, letter_bank):
    letter_dict = dict()

    for letter in letter_bank:
        if letter in letter_dict:              
            letter_dict[letter] +=1
        else:
            letter_dict[letter] = 1

# if rue if every letter in input word is available in the right quanities 
#  if letter in word not in player hand,  or has too much of(letter) compared to letter bank
    # return false
    # 
    for letter in word:
        if letter not in letter_bank:
            return False
        else:
            letter_dict[letter] -= 1
            if letter_dict[letter] < 0:
                return False
    return True
    


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass