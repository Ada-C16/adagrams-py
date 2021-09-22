import random

def build_letter_pool():
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
    return letter_pool

def build_letter_pool_list(letter_pool):
    list_letter_pool = []
    for letter, frequency in letter_pool.items():
        for i in range(frequency):
            list_letter_pool.append(letter)
    return list_letter_pool

def draw_letters():
    # Building a dictionary instead of hard coding into a list directly
    # Allows for efficiency when we ever need to change letter pool later
    letter_pool_dict = build_letter_pool()
    # Convert into a list to ensure weighted probability 
    letter_pool_list  = build_letter_pool_list(letter_pool_dict)
    
    letters = []
    while len(letters) < 10:
        chosen_letter = random.choice(letter_pool_list)
        letter_pool_list.remove(chosen_letter)
        letters.append(chosen_letter)
    return letters

# def build_letter_pool():
#     letter_pool = {
#     "A": ["A" for i in range(9)],
#     "B": ["B" for i in range (2)],
#     "C": ["C" for i in range (2)],
#     "D": ["D" for i in range (4)],
#     "E": ["E" for i in range (12)],
#     "F": ["F" for i in range (2)],
#     "G": ["G" for i in range (3)],
#     "H": ["H" for i in range (2)],
#     "I": ["I" for i in range (9)],
#     "J": ["J" for i in range (1)],
#     "K": ["K" for i in range (1)],
#     "L": ["L" for i in range (4)],
#     "M": ["M" for i in range (2)],
#     "N": ["N" for i in range (6)],
#     "O": ["O" for i in range (8)],
#     "P": ["P" for i in range (2)],
#     "Q": ["Q" for i in range (1)],
#     "R": ["R" for i in range (6)],
#     "S": ["S" for i in range (4)],
#     "T": ["T" for i in range (6)],
#     "U": ["U" for i in range (6)],
#     "V": ["V" for i in range (2)],
#     "W": ["W" for i in range (2)],
#     "X": ["X" for i in range (1)],
#     "Y": ["Y" for i in range (2)],
#     "Z": ["Z" for i in range (1)] }
#     return letter_pool

# def draw_letters():
#     letter_pool = build_letter_pool()

#     list_letter_pool = []
#     for letter_frequencies in letter_pool.values():
#         for i in range(len(letter_frequencies)):
#             list_letter_pool.append(letter_frequencies[i])
    
#     letters = []
#     while len(letters) < 10:
#         chosen_letter = random.choice(list_letter_pool)
#         list_letter_pool.remove(chosen_letter)
#         letters.append(chosen_letter)
#     return letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass