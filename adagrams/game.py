import random

def draw_letters():

    letter_list = ['A','A','A','A','A','A','A','A','A','B','B', 
    'C', 'C', 'D', 'D', 'D','D','E','E','E','E','E','E','E','E',
    'E','E','E','E','F','F','G','G','G','H','H','I','I','I', 
    'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M',
     'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T',
      'T','T','T','T','T', 'U', 'U', 'U', 'U', 'V', 'V', 'W','W', 'X', 'Y','Y','Z']
    letters = letter_list.copy()
    chosen_letters = []
    for i in range(10):
        letter = random.choice(letters)
        letters.remove(letter)
        chosen_letters.append(letter)
    return chosen_letters
        
    # letters = {
    #     'A': 9, 
    #     'B': 2, 
    #     'C': 2, 
    #     'D': 4, 
    #     'E': 12, 
    #     'F': 2, 
    #     'G': 3, 
    #     'H': 2, 
    #     'I': 9, 
    #     'J': 1, 
    #     'K': 1, 
    #     'L': 4, 
    #     'M': 2, 
    #     'N': 6, 
    #     'O': 8, 
    #     'P': 2, 
    #     'Q': 1, 
    #     'R': 6, 
    #     'S': 4, 
    #     'T': 6, 
    #     'U': 4, 
    #     'V': 2, 
    #     'W': 2, 
    #     'X': 1, 
    #     'Y': 2, 
    #     'Z': 1
    #     }   
    # dict_letters = letters.copy()
    # chosen_letters = []
    # for i in range(9):
    #     letter = random.choice(dict_letters.keys())
    #     chosen_letters.append(letter)
    #     dict_letters["letter"] += -1
    # return chosen_letters
        



    

    # loop 10 times
    # for i in range 10 
    # the letter that it chooses, take it out of the list and 

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass