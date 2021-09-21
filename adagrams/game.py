import random

def intialize_letter_pool():
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

def intialize_game_pieces(letter_pool):
    game_pieces = []
    for letter, quantity in letter_pool.items():
        for i in range(quantity):
            game_pieces.append(letter)
    return game_pieces

def draw_letters():
    letter_pool = intialize_letter_pool()
    game_pieces = intialize_game_pieces(letter_pool)
    letter_bank = []

    random.shuffle(game_pieces)
    for i in range(10):
        random_letter = game_pieces.pop()
        letter_bank.append(random_letter)
    
    return letter_bank

def uses_available_letters(word, letter_bank):
    word_letter_list = list(word)
    letter_bank_copy = letter_bank[:]

    for letter in word_letter_list:
        if letter not in letter_bank_copy:
            return False
        else:
            word_letter_list.remove(letter)
            letter_bank_copy.remove(letter)
    
    return True

def get_valid_word_from_user():
    user_word = input("Enter word here: ")
        # isalpha will also return False if any spaces are present or if string is empty
    if not user_word.isalpha():
        print("Try again. Please make sure your input contains only letters and no spaces!")
        get_valid_word_from_user()
    else:
        return user_word.upper()

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass