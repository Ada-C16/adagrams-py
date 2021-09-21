import random

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

def draw_letters():
    # 3 tests
    # no parameters
    # LETTER_POOL is a dictionary
    # Return an array of ten strings where each contain one letter 
    # and are randomly drawn from LETTER_POOL
    # Idea 1: 
    # Before pulling letters, multiple the keys by the values (frequency) and append to a list
    
    letter_pool_list = []
    for letter, frequency in LETTER_POOL.items():
        # letter_frequency = letter * frequency
        # letter_pool_list.append(letter_frequency)
    
        for i in range(frequency):
            letter_pool_list.append(letter)


    # Use random function to pull 10 random letters from letter list into a new list
    selected_letters = []
    for i in range(10):
        selection = random.choice(letter_pool_list)
        selected_letters.append(selection)
        letter_pool_list.remove(selection)

    return selected_letters

# import random
# d = {'VENEZUELA':'CARACAS', 'CANADA':'OTTAWA'}
# random.choice(list(d.values()))
    



def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass