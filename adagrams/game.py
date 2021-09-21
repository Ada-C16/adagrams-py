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

    letter_pool_list = []
    for letter, value in LETTER_POOL.items():
        letter_pool_list += letter * value

    random_numbers = random.sample(range(0, len(letter_pool_list)), 10)
    letter_bank = []
    for x in random_numbers:
        letter_bank.append(letter_pool_list[x])
    print(letter_bank)
    return letter_bank
    
def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass