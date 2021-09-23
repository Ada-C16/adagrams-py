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

def uses_available_letters(word, letter_bank):
    for char in word:
        if char in letter_bank:
            letter_bank.remove(char)
        else:
            return False
    
    # Adds back used letters do letter_bank is not changed
    i = 0
    for char in word:
        letter_bank.insert(i, char)
        i += 1
    return True

def build_score_chart():
    score_chart = {
        "A": 1,
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10
    }
    return score_chart

def score_word(word):
    score_chart = build_score_chart()

    score = 0
    cap_word = word.upper()
    
    for char in cap_word:
        if not char:
            return 0
        else:
            point = score_chart[char]
            score += point
    if 7 <= len(cap_word) <=10:
        return score + 8
    return score 

def get_highest_word_score(word_list):
    pass