import random

def draw_letters():
    letter_pool = {
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

    letters_drawn = []

    letter_pool_list = []
    for key in letter_pool:
        for idx in range(letter_pool[key]):
            letter_pool_list.append(key)

    while len(letters_drawn) != 10:
        random_entry = random.choice(letter_pool_list)
        letters_drawn.append(random_entry)
        letter_pool_list.remove(random_entry)
    return letters_drawn


def uses_available_letters(word, letter_bank):

    # is_letter_in_letter_bank = True
    letters_copy = letter_bank.copy()

    word_length = len(word)

    # while is_letter_in_letter_bank == True and word_length > 0:
    #     for letter in word:
    #         if letter in letters_copy:
    #             letters_copy.remove(letter)
    #             word_length -= 1
    #         else:
    #             is_letter_in_letter_bank = False
    #             break
    # return is_letter_in_letter_bank

# ALTERNATE OPTION
    try:
        while word_length > 0:
            for letter in word:
                if letter in letters_copy:
                    letters_copy.remove(letter)
                    word_length -= 1
                else:
                    raise ValueError
        return True
    except ValueError:
        return False

def score_word(word):
    
    score_chart = {
    
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
    }

    word = word.upper()
    total_points = 0

    for letter in word:
        total_points += score_chart[letter]
    if len(word) >= 7 and len(word) <= 10:
        total_points += 8
    
    return total_points

def get_highest_word_score(word_list):

    highest_scoring_word = ("",0)

    for word in word_list:
        score = score_word(word)
        if score > highest_scoring_word[1]:
            highest_scoring_word = (word, score)
        elif score == highest_scoring_word[1]:
            if len(word) == len(highest_scoring_word[0]) \
                or len(highest_scoring_word[0]) >= 10:
                continue
            if len(word) >= 10 \
                or len(word)< len(highest_scoring_word[0]):
                highest_scoring_word = (word, score)

    return highest_scoring_word
