import string
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
    """
    Build a hand of 10 letters for the user. Returns an array of strings
    with one letter in each string. The num of strings included in the array 
    cannot be more than the num alloted to that letter in the letter table
    """
    letters = []
    letter_count = {}
    for letter in range(10):
        letter = random.choice(string.ascii_uppercase)
        if letter not in letters:
            letter_count[letter] = 0
            letters.append(letter)
            letter_count[letter] = 1
        elif letter_count[letter] < LETTER_POOL[letter]:
            letters.append(letter)
            letter_count[letter] += 1
        
    return letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass