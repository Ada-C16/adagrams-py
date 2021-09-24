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

'''
We generated LETTERS_POOL from LETTERS_DICT using the following code so that we
would not have to run it every time draw_letters is called since the pool of 
letters will be a constant
LETTERS_POOL = []
for letter in LETTERS_DICT:
    letters_string = letter * LETTERS_DICT[letter]
    for letter in letters_string:
        LETTERS_POOL.append(letter)
'''
LETTERS_POOL = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', \
'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', \
'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', \
'I','I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', \
'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', \
'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', \
'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']

SCORES = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, 
    "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3, 
    "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1, 
    "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4, 
    "X": 8, "Z": 10}

def draw_letters():
    '''
    Returns a hand of 10 letters drawn randomly without replacement from the 
    letter pool
    '''
    return random.sample(LETTERS_POOL, 10)

def uses_available_letters(word, letter_bank):
    '''
    Checks if word uses only letters in the letter_bank (hand) and does not use 
    a letter more times than it appears in the letter_bank
    Returns True or False
    '''
    temp_letter_bank = letter_bank.copy()
    for letter in word:
        if letter in temp_letter_bank:
            temp_letter_bank.remove(letter)
        else:
            return False
    return True



def score_word(word):
    '''
    Returns score of word based on letter values in SCORES. If the length of the
    word is 7, 8, 9, or 10, then the word gets an additional 8 points.
    '''
    total = 0 
    if len(word) >= 7:
        total += 8
    total += sum(SCORES[letter] for letter in word.upper())      
    return total      


def get_highest_word_score(word_list):
    '''
    input: word_list 
    output:  (winning_word, score)
    Tie-breaker conditions will only work if there is a two-way tie and does not 
    account for 3+-way ties
    '''
    score_list = []
    index_highest_score = []
    for word in word_list: 
        score_list.append(score_word(word)) 
    highest_score = max(score_list)
    for i in range(len(score_list)):
        if score_list[i] == highest_score:
            index_highest_score.append(i)
    if len(index_highest_score) == 1:
        return word_list[index_highest_score[0]], score_list[index_highest_score[0]]
    else:
        if len(word_list[index_highest_score[0]]) == len(word_list[index_highest_score[1]]):
            return word_list[index_highest_score[0]], score_list[index_highest_score[0]]
        for index in index_highest_score:
            if len(word_list[index]) == 10:
                return word_list[index], score_list[index]
        if len(word_list[index_highest_score[0]]) < len(word_list[index_highest_score[1]]):
            return word_list[index_highest_score[0]], score_list[index_highest_score[0]]
        else:
            return word_list[index_highest_score[1]], score_list[index_highest_score[1]]