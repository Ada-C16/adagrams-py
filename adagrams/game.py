import random

def draw_letters():
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

    letters_drawn = []

    letter_pool_list = []
    for key in letter_pool:
        for idx in range(letter_pool[key]):
            letter_pool_list.append(key)

    while len(letters_drawn) != 10:
        random_entry = random.choice(letter_pool_list)
        letters_drawn.append(random_entry)
    return letters_drawn


    
    
    # * is array a list or dictionary which includes the qty + letters

    
    # create a data structure for the distribution of letters
    # while len of new data structure - list "letters" is < 10
    #   note to self - double check length of 10 actually means 10
    # use random() to pull a random letter
    #   check if random letter is in our dataset 
    # #   check if quantity is > 0
    # #    if yes then return letter to list "letters" as single letter strings
    # #      qty value of letter decrease by 1
    # #    if not - continue 
    # return list of drawn letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass