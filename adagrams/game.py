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
    user_word = input("Enter word here: ").replace(" ", "")
        # isalpha will also return False if any spaces are present or if string is empty
    if not user_word.isalpha():
        print("Try again. Please make sure your input contains only letters!")
        get_valid_word_from_user()
    else:
        return user_word.upper()

def initialize_letter_value_dictionary():
    letter_value_dictionary = {
        'A': 1, 
        'E': 1, 
        'I': 1, 
        'O': 1, 
        'U': 1, 
        'L': 1, 
        'N': 1, 
        'R': 1, 
        'S': 1, 
        'T': 1,
        'D': 2, 
        'G': 2,
        'B': 3, 
        'C': 3, 
        'M': 3, 
        'P': 3,
        'F': 4, 
        'H': 4,
        'V': 4, 
        'W': 4,
        'Y': 4,
        'K': 5,
        'J': 8, 
        'X': 8,
        'Q': 10,
        'Z': 10
    }
    return letter_value_dictionary

def score_word(word):
    letter_value_dictionary = initialize_letter_value_dictionary()
    sum = 0 
    for letter in word:
        sum += letter_value_dictionary[letter.upper()]

    if len(word) >= 7:
        sum += 8
    
    return sum


def get_highest_word_score(word_list):
    highest_score = score_word(word_list[0])
    winning_word = word_list[0]

    for index in range(1, len(word_list)):
        word = word_list[index]
        this_words_score = score_word(word)
        if this_words_score > highest_score:
            highest_score = this_words_score
            winning_word = word
        elif this_words_score == highest_score:
            if len(word) == 10 or len(winning_word) == 10:
                if len(word) == 10 and not len(winning_word) == 10:
                    winning_word = word
            elif len(word) < len(winning_word):
                winning_word = word 

    return (winning_word, highest_score)



