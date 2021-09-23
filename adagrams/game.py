import random
LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 
    'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 
    'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}

def draw_letters():
    """
    Build a hand of 10 letters for the user. Returns an array of strings
    with one letter in each string. The num of strings included in the array 
    cannot be more than the num alloted to that letter in the letter table
    """
    letter_to_draw = list(LETTER_POOL.keys())
    letters_drawn = []
    letter_count = {}
    for letter in random.sample(letter_to_draw, 10):
        if letter not in letters_drawn:
            letter_count[letter] = 0
            letters_drawn.append(letter)
            letter_count[letter] = 1
        elif letter_count[letter] < LETTER_POOL[letter]:
            letters_drawn.append(letter)
            letter_count[letter] += 1
        
    return letters_drawn

def uses_available_letters(word, letter_bank):
    for char in word: # word is the test because we're checking if these letters are valid to use
        if word.count(char) > letter_bank.count(char): # if there are more char than char in bank
            # return True
            valid = False
        else:
            valid = True
            # return False
    
    return valid
            # return False
        # elif char not in letter_bank:
        #     return False
        # else:
        #     return True


def score_word(word):
    """
    This function will calculate the user's score for their entered word.
    It needs to calculate a score that ignores the lettercase, takes into
    account an empty word, and gives extra points for longer words. 
    """
    # a dict may be better to easily access the score. 
    # could use ints as keys for the score and letters as the value
    pass

def get_highest_word_score(word_list):
    pass