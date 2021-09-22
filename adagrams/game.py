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
    # use a dictionary with the letter as the key and the number of instances/tiles as the value
    # make a copy of LETTER_POOL (shallow/deep) 
    all_letters = LETTER_POOL.copy()
    # initialize an empty array to hold strings (letters)
    drawn_letters = []
    # continue loop until the list has ten values
    while len(drawn_letters) < 10:
        # use random module to choose a random key
        letter = random.choice(list(all_letters))
        # if the value associated with the key is greater than 1, append letter to list and decrease value by 1
        if all_letters[letter] >= 1:
                drawn_letters.append(letter)
                all_letters[letter] -= 1

    return drawn_letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    word_list = []
    for letter in word:
        if letter in letter_bank_copy: 
            letter_bank_copy.remove(letter)
            word_list.append(letter)  
    if len(word_list)== len(word):
        return True
    else:
        return False 


def score_word(word):
    word = word.upper()
    one_point = ['A','E','I','O', 'U', 'L', 'N','R','S','T']
    two_point = ['D','G']
    three_point = ['B','C','M','P']
    four_point = ['F','H','V','W','Y']
    five_point = ['K']
    eight_point = ['J','X']
    ten_point = ['Q', 'Z']
    word_score = 0
    if len(word)>=7 and len(word)<11:
        word_score += 8
    
    for letter in word:
        if letter in one_point:
            word_score += 1
        elif letter in two_point:
            word_score += 2
        elif letter in three_point:
            word_score += 3
        elif letter in four_point:
            word_score += 4
        elif letter in five_point:
            word_score += 5
        elif letter in eight_point:
            word_score += 8
        elif letter in ten_point:
                word_score += 10
    return word_score


def get_highest_word_score(word_list):
    pass

