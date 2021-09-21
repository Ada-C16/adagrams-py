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

def uses_available_letters(word, letter_bank):
    
    #iterate through len(word)
    #for elem in word:
        #if elem in letter_bank:
            #if True, remove letter
        #else return False

    #return True

        #return True if every letter in word paramenter is in letter_bank
        #return False if letter is not in letter_bank or has too much letters
            #compared to letter_bank
    
    pass


###########################################################
                        # Wave 3 #
###########################################################

#make constant_dict of 
LETTER_SCORE = {}

def score_word(word):
    #intialize total_score
    total_score = 0
    
    #get letter score
    for elem in len(word):
        total_score += LETTER_SCORE[elem]

    # add 8 to total score if letter len is >= 7
    if len(word) >= 7:
        total_score += 8

    #returns total_score
    return total_score

    #make list comprehension 

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
    #get first min_len word

    #turn into tuple

    #return tuple that represents data of winning word and scores
        #   index 0 ([0]): a string of a word
        #   index 1 ([1]): the score of that word