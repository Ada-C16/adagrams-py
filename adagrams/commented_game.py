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

SCORE_CHART_DICT = {
        1 : ["A","E","I", "O", "U", "L", "N", "R", "S", "T"],
        2 : ["D", "G"],
        3 : ["B", "C", "M", "P"],
        4 : ["F", "H", "V", "W", "Y"],
        5 : ["K"],
        8 : ["J", "X"],
        10: ["Q", "Z"]
    }

def draw_letters():
    # 3 tests
    # no parameters
    # LETTER_POOL is a dictionary
    # Return an array of ten strings where each contain one letter 
    # and are randomly drawn from LETTER_POOL
    # Idea 1: 
    # Before pulling letters, multiple the keys by the values (frequency) and append to a list
    
    letter_pool_list = []
    for letter, frequency in LETTER_POOL.items():
        # letter_frequency = letter * frequency
        # letter_pool_list.append(letter_frequency)
    
        for i in range(frequency):
            letter_pool_list.append(letter)


    # Use random function to pull 10 random letters from letter list into a new list
    letter_bank = []
    for i in range(10):
        selection = random.choice(letter_pool_list)
        letter_bank.append(selection)
        letter_pool_list.remove(selection)

    return letter_bank

# Wave 2
# 4 tests
# 2 parameters (word and letter_bank)
# Idea 1:
# if yes, True and remove letter from letter_bank
# else false
# 
# Idea 2:
# for letter in word 
# Check if letter is in letter_bank
# word_value = []
# if yes, add letter to word_value and remove letter from letter_bank
# if no,

def uses_available_letters(word, letter_bank):
# letters_in_hand = ""
    letters_played = ""
# copy of letter_bank so that we don't change it
    letter_bank_copy = letter_bank.copy()
# for letter in word 
    for letter in word:
# Check if letter is in letter_bank
        if letter in letter_bank_copy:
# if yes, letters_played += letter and remove letter from bank
            letters_played += letter
            letter_bank_copy.remove(letter)
# if word == letters_played return True, if not, return False
    played_letters_in_hand = (word == letters_played)
    return played_letters_in_hand



def score_word(word):
# one parameter: word
# 4 tests
# Return an integar that is the number of points
# for each letter in word, check if letter is in 
# dict = {1 : [" A, E, I "]} -> ["A, E, I"] = dict[1]
# pointage = 0
# for key, value in dict.items():
    # if letter in dict[key]:
        # pointage += key
# if length of word is range 7 to 11, then add 8 points

    
    point_count = 0
    for letter in word.upper():
        for key, value in SCORE_CHART_DICT.items():
            if letter in SCORE_CHART_DICT[key]:
                point_count += key
    
    if len(word) in range(7, 11):
        point_count += 8
    
    return point_count

def get_highest_word_score(word_list):
    # one parameter word_list
    # 7 tests
    # create a dictionary of word : score key-value pairs
    word_and_score_dict = {}
    # max_score = 0
    max_score = 0
    # max_word = []
    max_word = []
    # for word in word_list, find score and add to dict
    for word in word_list:
        # is_ten = False
        # dict[word] = score
        score = score_word(word)
        word_and_score_dict[word] = score
        # if score > max_score 
        if score > max_score:
            # max_score = score
            max_score = score
            # max_word = [word]
            max_word = [word]
        # if score == max_score
        elif score == max_score:
            # append word to max_word
            max_word.append(word)
        # if len(word) = 10:
            # is_ten = True
    
    # tie breaking rules: 
    # if tie and same length, first one in word list wins
    if len(max_word) == 1:
        winning_word = max_word[0]
    elif len(max_word[0]) == len(max_word[1]):
        winning_word = max_word[0]
    # if tie and 10 letters, 10 letters wins. 
    # elif len(max_word[0]) == 10 or len(max_word[1]) == 10:
    elif len(max_word[0]) == 10:
        winning_word = max_word[0]
    elif len(max_word[1]) == 10:
        winning_word = max_word[1]
    # if all are less than 10 letters, shortest wins
    elif len(max_word[0]) < len(max_word[1]):
        winning_word = max_word[0]
    else:
        winning_word = max_word[1]

    winning_tuple = (winning_word, word_and_score_dict[winning_word])

    return winning_tuple


    # if max_word[0] is_ten or max_word[1]
    #for word in max_word
    #   if is_ten
        # winning_tuple = (word, dict[word])

    # return a tuple ("word", score)
