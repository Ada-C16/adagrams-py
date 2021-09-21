
import random

def draw_letters():

    LETTER_POOL = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 
        'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 
        'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 
        'Z': 1
    }

    # reconstructing LETTER_POOL into a list thats contains all of the 
    # possible letter choices.
    
    letter_choices = []
    expanded_letter_pool = []

    for alphabet, distribution in LETTER_POOL.items():
        if isinstance(distribution, (int)) == True:
            letter_choices.append(alphabet * distribution)

    letter_string = "".join(letter_choices)
    print(type(letter_string))

    for letter in letter_string:
        expanded_letter_pool.append(letter)
    
    # Selecting 10 letter from expanded_letter_pool to create letter_bank.
    letter_bank = random.sample(expanded_letter_pool, 10)
    
    return letter_bank


def uses_available_letters(word, letter_bank):
    pass


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass
