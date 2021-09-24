import random
import english_dictionary
from english_dictionary.scripts.read_pickle import get_dict
# This dictionary package is not a comprehensive list of all English words.
# The dictionary does not recognize suffixes, e.g. "voted" is not recognized, but "vote" is.
english_dict = get_dict()

LETTER_POOL = ["A", "A", "A", "A", "A", "A", "A", "A", "A", 
"B", "B", 
"C", "C", 
"D", "D", "D", "D", 
"E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
"F", "F", 
"G", "G", "G", 
"H", "H", 
"I", "I", "I", "I", "I", "I", "I", "I", "I", 
"J", 
"K", 
"L", "L", "L", "L", 
"M", "M",
"N", "N", "N", "N", "N", "N",
"O", "O", "O", "O", "O", "O", "O", "O",
"P", "P",
"Q",
"R", "R", "R", "R", "R", "R",
"S", "S", "S", "S",
"T", "T", "T", "T", "T", "T",
"U", "U", "U", "U",
"V", "V",
"W", "W",
"X",
"Y", "Y",
"Z"]

SCORE_CHART = {
    "A": 1,
    "E": 1,
    "I": 1,
    "O": 1,
    "U": 1,
    "L": 1,
    "N": 1,
    "R": 1,
    "S": 1,
    "T": 1,
    "D": 2,
    "G": 2,
    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,
    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10
}

def draw_letters():
    is_freq_correct = False
    #Loop to check if letter frequency is correct in relation to LETTER_POOL
    while is_freq_correct == False:
        letter_bank = random.choices(LETTER_POOL, k=10)
        # random.choices() documentation at https://docs.python.org/3/library/random.html
        is_freq_correct = True
        #Begin with assuming frequency is correct
        #print(letter_bank)
        for letter in letter_bank:
            if letter_bank.count(letter) > LETTER_POOL.count(letter):
                is_freq_correct = False
                #Letter frequency is incorrect. Breaks the loop and creates new hand of letter.
                break
    #print(f"After freq check {letter_bank}")
    return letter_bank

#for testing: draw_letters()

def uses_available_letters(word, letter_bank):
    word = word.upper()
    #Return True if every letter in input word is available (in the right quantities) in letter_bank
    for letter in word:
        if letter in letter_bank and word.count(letter) <= letter_bank.count(letter):
            continue
        else:
            #Will return False if input word uses letters not in letter_bank, 
            # and/or over the quantity of the letter available in letter_bank.
            return False
    return True

def score_word(word):
    word = word.upper()
    score = 0
    for letter in word:
        score += SCORE_CHART[letter]
    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):

    highest_score = 0
    highest_words = []
    for word in word_list:
        score = score_word(word)
        if highest_score < score:
            highest_score = score
            highest_words = [word]
        elif highest_score == score:
            highest_words.append(word)

    if len(highest_words) == 1: # This means that there is no tie
        return(highest_words[0], highest_score)
    else:                       # This means there is a tie, applies tie-breaking logic
        for word in highest_words:
            if len(word) == 10:
                return(word, highest_score)
        return(min(highest_words, key=len), highest_score)

def word_in_english_dictionary(word):
    word = word.lower()
    if word in english_dict.keys():
        return True
    else:
        return False
