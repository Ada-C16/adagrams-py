import random
LETTER_POOL = {
    'A': 5, 
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
    LETTER_POOL_LIST = []  
    for letter in LETTER_POOL.keys():
        for count in range(LETTER_POOL[letter]):
            LETTER_POOL_LIST.append(letter)
    
    letters = []
    while len(letters) < 10:
        letter = random.choice(LETTER_POOL_LIST)
        letters.append(letter)
        LETTER_POOL_LIST.remove(letter)
    return letters

def uses_available_letters(word, letter_bank):
    matched_list=[characters in letter_bank for characters in word]
    string_contains_chars = all(matched_list)
    return string_contains_chars


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass