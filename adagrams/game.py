import random
import copy    


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
    
    temp_letter_pool = copy.deepcopy(LETTER_POOL)
    letter_list_from_pool = list(LETTER_POOL.keys())
    letter_not_found = True
    letters_drawn_list = []
    
    letter = ""
    
    for draw in range(10):
        
        # need this flag when exiting while loop to search for other letter
        letter_not_found = True
        
        while letter_not_found:
            letter = random.choice(letter_list_from_pool)
            letter_count = temp_letter_pool[letter]
            
            # this conditional checks that there's a letter available and changes the flag to letter found
            if letter_count > 0:
                letter_not_found = False
                
        letters_drawn_list.append(letter)
        # decrement count temp letter pool
        temp_letter_pool[letter] -= 1
    
    return letters_drawn_list

def uses_available_letters(word, letter_bank):
    letter_bank_letter_count = {}
    for letter in letter_bank:
        if letter in letter_bank_letter_count:
            letter_bank_letter_count[letter] += 1
        else:
            letter_bank_letter_count[letter] = 1

    for letter in word:
        # if a letter in word is in the letter_bank, 
        # then remove one of the counts from the letter tally in the dict
        # to signify that letter in the letter_bank has been taken
        if letter in letter_bank_letter_count and letter_bank_letter_count[letter] > 0:
            letter_bank_letter_count[letter] -= 1
        else:
            return False

    return True


def score_word(word):
    word = word.lower()
    
    SCORE_CHART = {
    'a': 1, 
    'b': 3, 
    'c': 3, 
    'd': 2, 
    'e': 1, 
    'f': 4, 
    'g': 2, 
    'h': 4, 
    'i': 1, 
    'j': 8, 
    'k': 5, 
    'l': 1, 
    'm': 3, 
    'n': 6, 
    'o': 1, 
    'p': 3, 
    'q': 10, 
    'r': 1, 
    's': 1, 
    't': 1, 
    'u': 1, 
    'v': 4, 
    'w': 4, 
    'x': 8, 
    'y': 4, 
    'z': 10
}


    word_score = 0

    for letter in word:
        word_score += SCORE_CHART[letter]  
        
    if 6 < len(word) < 11:
        word_score += 8
    
    return word_score

def get_highest_word_score(word_list):
    pass