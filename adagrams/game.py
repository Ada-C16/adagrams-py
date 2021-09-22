import random
def draw_letters():
    # Initialize variables
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
    # Declare variables
    bank_in_action = [] 
    # Deep copy letter_bank
    for letter in letter_bank:
        bank_in_action.append(letter)
    # Check for, and update letter bank copy
    for each in word:
        if each in bank_in_action:
            bank_in_action.remove(each)
        else:
    # Return False if insufficient letters, otherwise True
            return False
    return True

def score_word(word):
    # Initialize and Sanitize variables
    score = 0
    word = word.upper()
    # Scoring for length
    if len(word) > 6:
        score += 8
    # Scoring for each letter.  Could also be list variables. 
    for letter in word:
        if letter in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T",]:
            score += 1
        elif letter in ["D", "G", "", "", "", "", "", "", "", "",]:
            score += 2
        elif letter in ["B", "C", "M", "P", "", "", "", "", "", "",]:
            score += 3
        elif letter in ["F", "H", "V", "W", "Y", "", "", "", "", "",]:
            score += 4
        elif letter in ["K", "", "", "", "", "", "", "", "", "",]:
            score += 5
        elif letter in ["J", "X", "", "", "", "", "", "", "", "",]:
            score += 8
        elif letter in ["Q", "Z", "", "", "", "", "", "", "", "",]:
            score += 10
    # Return total score
    return score
            
def get_highest_word_score(word_list):
    # Initialize variables
    score_tuples  = []
    current_high_score = 0
    winning_word_length = 0
    # Iterate through each word
    for word in word_list:
        #check for new high score
        if score_word(word) > current_high_score:
            current_high_score = score_word(word)
            winning_word_length = len(word)
            score_tuples = ((word, score_word(word)))
        # If tied for high score
        if score_word(word) == current_high_score:
            if len(word) < winning_word_length and winning_word_length != 10:
                score_tuples = ((word, score_word(word)))
                winning_word_length = len(word)
            # Length 10 edge case
            elif len(word) == 10 and winning_word_length != 10:
                score_tuples = ((word, score_word(word)))
                winning_word_length = len(word)
    #return high score as tuple 
    return score_tuples