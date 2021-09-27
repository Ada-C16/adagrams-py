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

LETTER_VALUES = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def draw_letters():
    letters_left = LETTER_POOL.copy() 
    choice_ten = [] 
    while len(choice_ten) < 10: 
        letter = random.choice(list(letters_left)) 
        if letters_left[letter] > 0: 
            choice_ten.append(letter) 
            letters_left[letter] -= 1 
    return choice_ten
        
        

def uses_available_letters(word, choice_ten):
    letters_in_hand = choice_ten.copy() 
    for letter in word:
        if letter in letters_in_hand:
            letters_in_hand.remove(letter)
        else:    
            return False
    return True

def score_word(word):
    total = 0
    for letter in word:
        total += LETTER_VALUES[letter.upper()]
    if len(word) >= 7:
        total += 8
    
    return total

def get_highest_word_score(word_list):
    top_word = None
    top_score = 0 
    for word in word_list: 
        score = score_word(word)
        if score < top_score:
            pass
        elif score > top_score:
            top_word = word
            top_score = score
        elif score == top_score:
            if len(word) == len(top_word):
                pass
            elif len(top_word) == 10: 
                pass
            elif len(word) == 10:
                top_word = word
                top_score = score
            elif len(word) < len(top_word): 
                top_word = word
                top_score = score
    return top_word, top_score          

    

    
            