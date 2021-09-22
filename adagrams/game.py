import random 

LETTERS_DICT = {
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
    ''' 
    1. No parameters
    2. returns an arrary of 10 strings 
        2a. each should contain only one letter (so returns ten letters)
    3. Ltrs should be randomly drawn from a pool of ltrs 
        3a. see table in read me, pool should reflect same
        3b. #random.sample(function)  - random.sample(list, # of elements to pick) (selects elements w/o replacement)
    4. this function should NOT change the pool of ltrs (user returns hand before drawing) unlike scrabble where pool decreases until it runs out
    '''


    
    pass
    #pseudocode
    # letters_pool = []iterate through dict to make list?
        # for letter in letters_dict: 
        # mulitply each key x value 
        #thought 1. 
            # [key * val for key, val in letters_dict.items()] 
            # returns strings per character ex "AAAAAAAAAA"
            # loop through to create list of strings? 

    letters_pool = []
    for letter in LETTERS_DICT:
        letters_string = letter * LETTERS_DICT[letter]
        for letter in letters_string:
            letters_pool.append(letter)
    hand = random.sample(letters_pool, 10)
    return hand


def uses_available_letters(word, letter_bank):
    pass

SCORES = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, 
    "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3, 
    "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1, 
    "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4, 
    "X": 8, "Z": 10}

def score_word(word):
    '''
    returns the score of a given word as defined by the adagrams game
    1. input parameter: word (str of chars)
    2. returns an int representing the no. of points

    #Each letter within `word` has a point value. 
    #The number of points of each letter is summed up to represent the total score of `word`
    ~~~~~~If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
    '''
    # return sum(SCORES[letter] for letter in word) 
    # would like to refactor to the above 

    total = 0 
    # for char in word: 
    if len(word) >= 7:
            total +=8   
    # for letter in word.upper():       
    #     total += SCORES[letter]  
    total += sum(SCORES[letter] for letter in word.upper())      
    return total      



def get_highest_word_score(word_list):
    '''
    
    '''
    pass