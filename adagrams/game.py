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
    # initialize list of letters
    chosen_letters = []
    remaining_letters_count = 0
    for letter, count in LETTER_POOL.items():
        remaining_letters_count += count
    if remaining_letters_count >= 10:
    # do this 10 times:
        while len(chosen_letters) != 10:
            # from letter bank select random letter
            drawn_letter = key, value = random.choice(list(LETTER_POOL.items()))
            # check value of letter is not zero
            if LETTER_POOL[drawn_letter[0]] != 0:
                # add letter to list
                chosen_letters.append(drawn_letter[0])
                # if chosen, decrease value by 1
                LETTER_POOL[drawn_letter[0]] -= 1
    return chosen_letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass