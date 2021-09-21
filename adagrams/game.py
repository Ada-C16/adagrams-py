import random 

def draw_letters():
    letter_pool = ['A','A','A','A','A','A','A','A','A',
    'B','B', 'C','C', 'D','D','D','D',
    'E','E','E','E','E','E','E','E','E','E','E','E', 
    'F','F','G','G','G', 'H','H', 'I','I','I','I','I','I','I','I','I',
    'J', 'K', 'L','L','L','L', 'M','M', 'N','N','N','N','N','N',
    'O','O','O','O','O','O','O','O', 'P','P', 'Q', 'R','R','R','R','R','R',
    'S','S','S','S', 'T','T','T','T','T','T', 'U','U','U','U',
    'V','V', 'W','W', 'X', 'Y','Y','Z']
    player_hand = random.sample(letter_pool, k=10)
    return player_hand


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass