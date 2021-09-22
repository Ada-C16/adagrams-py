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

    possible_letters = dictionary_to_list(letter_pool)

    player_hand = random.sample(possible_letters, 10)
    return player_hand

def uses_available_letters(word, letter_bank):
    word = word.upper()

    letter_dict = dict()

    for letter in letter_bank:
        if letter in letter_dict:              
            letter_dict[letter] +=1
        else:
            letter_dict[letter] = 1

    for letter in word:
        if letter not in letter_bank:
            return False
        else:
            letter_dict[letter] -= 1
            if letter_dict[letter] < 0:
                return False
    return True

def score_word(word):
    
    player_score = 0

    score_chart =  {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2,
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10,
    }
    word = word.upper()

    for letter in word:
        player_score += score_chart[letter]
    if len(word) in range(7, 11):
        player_score += 8
    return player_score
    
def get_highest_word_score(word_list):
    words_scores_list = []

    for word in word_list:
        word_score = score_word(word)
        words_scores_list.append((word, word_score))
    
    winning_word = ""
    high_score = 0

    for word, word_score in words_scores_list:
        if word_score > high_score:
            winning_word = word
            high_score = word_score
        elif word_score == high_score:
            if len(winning_word) == 10:
                continue
            elif len(word) == 10:
                winning_word = word
                high_score = word_score
            elif len(word) < len(winning_word):
                winning_word = word
                high_score = word_score
            elif len(word) == len(winning_word):
                continue
        
    return (winning_word, high_score)
