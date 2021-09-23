
import random
def draw_letters():
    letter_pool = {}
    #deep-copy of letter_pool to prevent it from changing as we withdraw letters from it


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

    score_of_points = 0

    score_chart = {
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

    word = word.upper()
    

    for letter in word:
        score_of_points += score_chart[letter]
    if len(word) in range(7,11):
        score_of_points += 8
    return score_of_points




def get_highest_word_score(word_list):
    pass