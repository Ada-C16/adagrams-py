# from tests.test_wave_01 import LETTER_POOL
import random
# Wave 1

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
    # Transforming LETTER_POOL dictionary into a list
    all_letters = []
    for letter, quantity in LETTER_POOL.items():
        for i in range(quantity):
            all_letters.append(letter)

    letter_bank = []
    # Adding 10 random letters to user's letter_bank
    for i in range(10):
        random_int = random.randint(0, len(all_letters)-1)
        letter_bank.append(all_letters[random_int])
        all_letters.pop(random_int)

    return letter_bank

draw_letters()

# Wave 2
def uses_available_letters(word, letter_bank):
    pass

# Wave 3
def score_word(word):
    pass

# Wave 4
def get_highest_word_score(word_list):
    pass

# Mariah's comment added 9/20
# Sarah's comment 9/20