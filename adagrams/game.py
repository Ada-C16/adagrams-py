import random

###########################################################
                        # Wave 1 #
###########################################################

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

#create helper function
def build_letter_pool():
    #intialize variables
    letter_pool_list = []

    for key in LETTER_POOL:
        letter_pool_list.extend([key] * LETTER_POOL[key])
    return letter_pool_list


def draw_letters():
    #build a list of all the letters
    letter_pool_list = build_letter_pool()
    letter_bank = []

    #iterate for size of user_hand
    #generate random index for letter_pool_list
    for i in range(10):
        index = random.randint(0, len(letter_pool_list)-1)
        letter_bank.append(letter_pool_list[index])
        letter_pool_list.remove(letter_pool_list[index])

    return letter_bank


###########################################################
                        # Wave 2 #
###########################################################

#
def uses_available_letters(word, letter_bank):
    #make copy of letter_bank
    letter_bank_copy = letter_bank.copy()

    #loops through each character in word, removes char in letter_bank_copy
    #returns boolean
    for char in word:
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False

    return True

###########################################################
                        # Wave 3 #
###########################################################

#make constant_dict for letter_score
LETTER_SCORE = {
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

#returns total_score of word
def score_word(word):
    #intialize total_score
    total_score = 0
    
    #get letter score
    for char in word:
        total_score += LETTER_SCORE[char.upper()]

    # add 8 to total score if letter len is >= 7
    if len(word) >= 7:
        total_score += 8

    #returns total_score
    return total_score

###########################################################
                        # Wave 4 #
###########################################################

def get_highest_word_score(word_list):
    
    #initialize variables
    max_score = 0
    highest_scoring_words = []

    #build list of highest scoring words
    for word in word_list:
        if score_word(word) > max_score:
            highest_scoring_words = [word]
            max_score = score_word(word)
        elif score_word(word) == max_score:
            highest_scoring_words.append(word)

    #check for tie breaks
    if len(highest_scoring_words) > 1:
        for word in highest_scoring_words:
            #check for ten word length
            if len(word) == 10:
                return word, max_score

    #returns shortest word and max_score
    return min(highest_scoring_words, key=lambda a : len(a)), max_score