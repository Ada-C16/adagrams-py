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
    # use a dictionary with the letter as the key and the number of instances/tiles as the value
    # make a copy of LETTER_POOL (shallow/deep) 
    all_letters = LETTER_POOL.copy()
    # initialize an empty array to hold strings (letters)
    drawn_letters = []
    # continue loop until the list has ten values
    while len(drawn_letters) < 10:
        # use random module to choose a random key
        letter = random.choice(list(all_letters))
        # if the value associated with the key is greater than 1, append letter to list and decrease value by 1
        if all_letters[letter] >= 1:
                drawn_letters.append(letter)
                all_letters[letter] -= 1

    return drawn_letters

def uses_available_letters(word, letter_bank):
    
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

