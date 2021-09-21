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
    letter_bank = []
    for i in range(10):
        selection = random.choice(letter_pool_list)
        letter_bank.append(selection)
        letter_pool_list.remove(selection)

    return letter_bank

# Wave 2
# 4 tests
# 2 parameters (word and letter_bank)
# Idea 1:
# if yes, True and remove letter from letter_bank
# else false
# 
# Idea 2:
# for letter in word 
# Check if letter is in letter_bank
# word_value = []
# if yes, add letter to word_value and remove letter from letter_bank
# if no,

def uses_available_letters(word, letter_bank):
# letters_in_hand = ""
    letters_played = ""
# copy of letter_bank so that we don't change it
    letter_bank_copy = letter_bank.copy()
# for letter in word 
    for letter in word:
# Check if letter is in letter_bank
        if letter in letter_bank_copy:
# if yes, letters_played += letter and remove letter from bank
            letters_played += letter
            letter_bank_copy.remove(letter)
# if word == letters_played return True, if not, return False
    played_letters_in_hand = (word == letters_played)
    return played_letters_in_hand



def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass