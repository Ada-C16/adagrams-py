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
    letters_pool = []
    for letter in LETTERS_DICT:
        letters_string = letter * LETTERS_DICT[letter]
        for letter in letters_string:
            letters_pool.append(letter)
    hand = random.sample(letters_pool, 10)
    return hand

def uses_available_letters(word, letter_bank):
    '''
    check if word uses only characters in the letter_bank (hand) and does not use
    a letter more times than it appears in the letter_bank
    return True or False
    '''
    # Make copy of letter_bank to be able to manipulate
    # Iterate through word check if each letter is in letter_bank copy and remove
    # from copy
    # If not in, return False
    # If make it all the way through, return True
    temp_letter_bank = letter_bank.copy()
    for letter in word:
        if letter in temp_letter_bank:
            temp_letter_bank.remove(letter)
        else:
            return False
    return True

SCORES = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, 
    "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3, 
    "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1, 
    "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4, 
    "X": 8, "Z": 10}

def score_word(word):
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
    input: word_list 
    output:  (winning_word, score)
    this will only work if there is a two-way tie
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
        for index in index_highest_score:
            if len(word_list[index]) == 10:
                return word_list[index], score_list[index]
        if len(word_list[index_highest_score[0]]) < len(word_list[index_highest_score[1]]):
            return word_list[index_highest_score[0]], score_list[index_highest_score[0]]
        elif len(word_list[index_highest_score[0]]) > len(word_list[index_highest_score[1]]):
            return word_list[index_highest_score[1]], score_list[index_highest_score[1]]
