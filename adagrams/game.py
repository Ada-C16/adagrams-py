import random 
LONG_WORD_MIN = 7
LONG_WORD_MAX = 10
LONG_WORD_POINTS = 8

# Wave 1
def build_letter_pool():
    """This function returns a dictionary of the letter pool
    by assigning the letter as the key and the distribution of each
    corresponding letter as the value."""
    letter_pool = {
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
    return letter_pool

def build_letter_pool_list(letter_pool):
    """This function takes the dictionary of the letter pool and returns
    a list of strings that represents the distribution of letters in the 
    letter pool."""
    list_letter_pool = []
    for letter, frequency in letter_pool.items():
        for i in range(frequency):
            list_letter_pool.append(letter)
    return list_letter_pool

def draw_letters():
    """This function returns an array of ten strings, where each string
    represents a letter and the array represents the hand of letters the
    player has drawn."""
    letter_pool_dict = build_letter_pool()
    # Convert into a list to ensure weighted probability 
    letter_pool_list  = build_letter_pool_list(letter_pool_dict)
    # Random sample function returns list of K size
    player_hand = random.sample(letter_pool_list, k=10) 
    return player_hand

# Wave 2
def uses_available_letters(word, letter_bank):
    """This function returns True if every letter in the input word
    is available in the right quantities from the letter bank. Otherwise,
    it returns False."""
    letter_bank_copy = letter_bank.copy()
    for char in word:
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False
    return True
    

def build_score_chart():
    """This function returns a dictionary of the score chart, by
    assigning the letter as the key and the number of points for each
    corresponding letter as the value."""
    score_chart = {
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
    return score_chart

def score_word(word):
    """This function returns an integer that represents the number of points 
    awarded for a given word"""
    score_chart = build_score_chart()
    score = 0
    cap_word = word.upper()
    
    for char in cap_word:
        if not char:
            return 0
        else:
            point = score_chart[char]
            score += point
    if LONG_WORD_MIN <= len(cap_word) <=LONG_WORD_MAX:
        return score + LONG_WORD_POINTS
    return score 

def get_highest_word_score(word_list):
    """This function returns a tuple that represents the data of a
    winning word and its respective score given a list of words. This function
    also applies tie-breaking logic to determine the winning word and score"""
    all_points = get_all_points(word_list)
    max_score = max(all_points)
    index_value = None 
    
    if not check_if_tie_case(all_points, word_list):
        index_value = get_index_from_list(all_points, max_score)
        return word_list[index_value], max_score
    
    # All code below refer to tie-breaking cases
    # When all words have different lengths but none of the words has 10 letters
    if not check_if_same_length(word_list) and not check_if_any_word_is_ten(word_list):
        word_lengths = get_word_lengths(word_list)
        shortest_word = min(word_lengths)
        index_value = get_index_from_list(word_lengths, shortest_word)
        return word_list[index_value], max_score
        
    # When we have a 10-letter word, return the first 10-letter word in the list 
    # Combines second and third conditions for tie-breaking rules
    if check_if_any_word_is_ten(word_list):
        word_lengths = get_word_lengths(word_list)
        index_value = get_index_from_list(word_lengths, 10)
        return word_list[index_value], max_score

# Helper functions for wave 4
def get_all_points(word_list): 
    """This function returns a list of integers, with 
    each integer representing the score for each word in the
    list of words"""
    all_points = [score_word(word) for word in word_list]
    return all_points

def check_if_tie_case(all_points, word_list):
    """This function returns True when there is a tie.
    Otherwise, the function returns False."""
    if len(set(all_points)) != len(word_list):
        return True
    return False

def get_index_from_list(any_list, any_value):
    """This function returns the index of any_value from 
    any_list"""
    for i in range(len(any_list)):
        if any_list[i] == any_value:
            return i

def get_word_lengths(word_list):
    """This function return a list of integers, with each 
    integer as the length of each word"""
    word_lengths = [len(word) for word in word_list]
    return word_lengths

def check_if_same_length(word_list):
    """Returns true if all words from a list of words are
    the same lengths. Otherwise, the function returns False."""
    word_length = get_word_lengths(word_list)
    if len(set(word_length)) != len(word_list):
        return True
    return False

def check_if_any_word_is_ten(word_list):
    """ This function returns true if any word from a list of 
    words has 10 letters"""
    word_length = get_word_lengths(word_list)
    if 10 in word_length:
        return True
    return False