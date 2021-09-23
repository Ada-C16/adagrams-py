
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
    
    for letter in word:
        if letter in letter_bank: #account for letter frequency {}
            return True
        else:
            return False

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass