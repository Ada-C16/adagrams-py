
import random
def draw_letters():
    LETTER_POOL = {}

    letter_bank = []
    letter_list = list(LETTER_POOL.keys())

#loop through letter_pool to get 10 random letters and append them to the letter_bank list
    for letter in LETTER_POOL:
        random_letter = random.sample(letter_list, 10)
        letter_bank.append(random_letter)
    return letter_bank
#def function_2:
#letter_freq = {}

#for letter in letters:
    #if letter in letter_freq:
        #letter_freq[letter] += 1
    #else:
        #letter_freq[letter] = 1


def uses_available_letters(word, letter_bank):
    letter_frequency = {}
    
    for letter in letter_bank:
        if letter in letter_frequency: 
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
            
    for letter in word:
        if letter not in letter_bank:
            return False
        else:
            letter_frequency[letter] -= 1
            if letter_frequency[letter] < 0:
                return False
    return True

def score_word(word):
    
    score_chart ={
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
    word_dict = {}
    for letter in word:
        word_dict.append[letter]

    score_of_points = 0

    for letter in word:
        score_of_points =+ score_chart[letter]
    if len(word) >= 7 and len(word) <= 10:
        score_of_points += 8
    return score_of_points

def get_highest_word_score(word_list):
    pass