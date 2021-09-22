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
        
        #need this flag when exiting the while loop to search for other letter
        letter_not_found = True
        
        while letter_not_found:
            letter = random.choice(letter_list_from_pool)
            letter_count = temp_letter_pool[letter]
            
            #this conditional checks that there's a letter available and changes the flag to letter found
            if letter_count > 0:
                letter_not_found = False
                
        letters_drawn_list.append(letter)
        # decrement count temp letter pool
        temp_letter_pool[letter] -= 1
    
    return letters_drawn_list

# def uses_available_letters(word, letter_bank):
#     pass

# def score_word(word):
#     pass

# def get_highest_word_score(word_list):
#     pass