###########################################################
                        # Wave 1 #
###########################################################

def draw_letters():
    #build a list of all the letters
    letter_pool_list = [0, 1, 10, 5]
    letter_bank = []

    #outter loop that will iterate 10 times
        #random number generator that pulls from the len of letter_pool_list
        #random number is index of the letter pool list
        #append user_hand with list value associate with random index
        #user_hand.append(letter_pool_list[i])
            #value from above
            #remove value from letter pool list
        #subtract -1 from range 

    return letter_bank

#create helper function
def _______():
    #use LETTER_POOL_dict 
    #iterate each key
    #append key to list as many times as value
    pass


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
    tied_words = []

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
                tied_words.append(word)
            #compare length for fewest letters

            #elif 
        #prefer the word with fewest letters
            #unless word has exactly 10 letters
            
        #

    #turn into tuple

    #return tuple that represents data of winning word and scores
        #   index 0 ([0]): a string of a word
        #   index 1 ([1]): the score of that word
    
    return highest_scoring_words[0], score_word(highest_scoring_words[0])