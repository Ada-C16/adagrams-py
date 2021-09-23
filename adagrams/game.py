import random

def draw_letters():

    letter_bank = {
    "A" : 9,
    "B" : 2,
    "C" : 2,
    "D" : 4,
    "E" : 12,
    "F" : 2,
    "G" : 3,
    "H" : 2,
    "I" : 9,
    "J" : 1,
    "K" : 1,
    "L" : 4,
    "M" : 2,
    "N" : 6,
    "O" : 8,
    "P" : 2,
    "Q" : 1,
    "R" : 6,
    "S" : 4,
    "T" : 6,
    "U" : 4,
    "V" : 2,
    "W" : 2,
    "X" : 1,
    "Y" : 2,
    "Z" : 1,
    }
    # Initialize variables
    letter_bank_keys = letter_bank.keys()
    letter_bank_copy = letter_bank.copy()
    letters = []
    hand_size = 0

    # Hand draw logic, including incrementer and non-zero value check
    while hand_size < 10:
        letter = random.choice(list(letter_bank_keys))
        if letter_bank_copy[letter] > 0:
            letters.append(letter)
            letter_bank_copy[letter] -= 1
            hand_size += 1

    return letters

def uses_available_letters(word, letter_bank):
    letter_bank = draw_letters()
    letter_bank_copy = letter_bank.copy()
    for char in letter_bank_copy:
        for char in word:
            if char not in letter_bank_copy:
                return False
            elif char in letter_bank_copy and word.count(char) == letter_bank_copy.count(char):
                return True
            else:
                return False
    
    # matches = [char in letter_bank_copy for char in word]
    # letter_bank_contains_word = all(matches)
    # return letter_bank_contains_word
def score_word(word):
    # Initialize and Sanitize variables
    score = 0
    word = word.upper()
    # Scoring for length
    # Scoring for each letter.  Could also be list variables. 
    # Return total score

def get_highest_word_score(word_list):
    score_tuples = ()
    # Initialize variables
    # Iterate through each word
    # Check for new high score
    # If tied for high score
    # Length 10 edge case
    #return high score as tuple 
    return score_tuples