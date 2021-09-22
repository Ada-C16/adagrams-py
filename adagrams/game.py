import random

def draw_letters():
    pool_of_letters = {
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

    list_of_letters = list(pool_of_letters.keys())

    draw_ten = []




    for i in range(10):
        random_letter = random.randint(0, 25)
        letter = list_of_letters[random_letter]
        
        while pool_of_letters[letter] == 0:
            random_letter = random.randint(0, 25)
            letter = list_of_letters[random_letter]
        
        draw_ten.append(letter)
        pool_of_letters[letter] -= 1

        
    return draw_ten



def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass