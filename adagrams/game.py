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
    # random sample function returns list of K size
    player_hand = random.sample(letter_pool, k=10) 
    return player_hand


def uses_available_letters(word, letter_bank):
    invalid = []
    for letter in word:
        if letter not in letter_bank or (word.count(letter) > letter_bank.count(letter)):
            invalid.append(letter)
    if len(invalid) > 0:
        return False 
    else:
        return True 

def score_word(word):
    
    letter_values = {
    1:['A','E','I','O','U','L','N','R','S','T'],
    2:['D','G'],
    3:['B','C','M','P'],
    4:['F','H','V','W','Y'],
    5:['K'],
    8:['J','X'],
    10:['Q','Z'],
    }
    lng_wrd_pnts = 8
    score = 0
    cap_word = word.upper()
    for letter in cap_word:
        for key,val in letter_values.items():
            if letter in val:
                score += key
    if len(cap_word) >= 7 and len(cap_word) <= 10:
        score += lng_wrd_pnts

    return score

def get_highest_word_score(word_list):
    pass