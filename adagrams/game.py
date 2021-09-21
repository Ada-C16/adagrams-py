import random

def initialize_letter_list():
    """ 
    Initialize the letter tuple for game based on "LETTER_POOL" dictionary. This dictionary has the count for each letter as the value.
    """
    # Letter dict
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
    # creating letter tuple, starting with a list data type in order to append
    letter_list = []
    for letter, count in LETTER_POOL.items():
        for i in range(count):
            letter_list.append(letter)
    return tuple(letter_list)

def draw_letters(letter_choices = initialize_letter_list()):
    # 1. Initialize list of letters
    # 2. Draw 10 letters
    letters_drawn = random.sample(letter_choices, 10)
    # 3. Return 10 letters (as str elements)
    print(letters_drawn)
    return letters_drawn

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

draw_letters()