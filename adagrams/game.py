import random

def initialize_letter_list():
    """ 
    Initialize the letter tuple for game based on "LETTER_POOL" dictionary. This dictionary has the count for each letter as the value.
    """
    # Letter dict
    LETTER_POOL_DICT = {
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
    # creating letter tuple, starting with a list data type in order to append
    letter_list = []
    for letter, count in LETTER_POOL_DICT.items():
        for i in range(count):
            letter_list.append(letter)
    return tuple(letter_list)

def draw_letters(letter_choices = initialize_letter_list()):
    """
    Choose 10 letters from letter_choices tuple for user to create words with.
    """
    # This random.sample() function takes two arguments, our tuple and number of selections. 
    # The ".sample" funtion randomly selects letters without replacement and returns a list.
    letters_drawn_list = random.sample(letter_choices, 10)
    
    # Return 10 letters (as str elements)
    return letters_drawn_list

def uses_available_letters(word, letter_bank):
    """
    Checks if user input, "word", is in the the letters they were provided. 
    """
    # copying letter_bank so it stays unchaged and doesn't produce side effects
    working_bank_list = letter_bank.copy()

    # looking at each letter in user input, "word", and seeing if it is in working_bank
    # remove letter from working_bank to prevent duplicates 
    # return false if user guesses letter that is not in working_bank
    for letter in word: 
        if letter in working_bank_list: 
            working_bank_list.remove(letter)
        else: 
            return False 
    
    return True

def score_word(word):
    """
    Returns score of user word per values in letters_value_dict
    """
    # Initialize dictionary with letter values
    letters_value_dict = {
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
    # Initialize sum variable
    sum = 0
    # Change user input to uppercase
    word = word.upper()
    # Loop through each letter in word and find value to add to sum
    for letter in word:
        sum += letters_value_dict.get(letter)
    # Add 8 to sum if word is longer than 6
    if len(word) > 6:
        sum += 8
    # return sum
    return sum

def tie_breaker(same_score_dict, word_list):
    """
    Returns winning word in the event of a tie.
    """
    # Get a list of tie words 
    same_score_words_list = list(same_score_dict.keys())

    # Initializing list variables to hold tie words
    ten_length_words_list = []
    min_length_words_list = []
 
    # Get min length of tie words
    min_length = len(min(same_score_words_list, key=len))

    # Make list for words with 10 char or min length 
    for word in same_score_words_list: 
        if len(word) == 10:
            ten_length_words_list.append(word)
        elif len(word) == min_length: 
            min_length_words_list.append(word)
    
    # If tie word is 10 char, returns first 10 char word as winner.
    # Otherwise return first shortest word as winner. 
    if len(ten_length_words_list) == 1: 
        return ten_length_words_list[0],same_score_dict[ten_length_words_list[0]]
    elif len(ten_length_words_list) > 1:
        for word in word_list: 
            if word in ten_length_words_list:
                return word, same_score_dict[word]
    elif len(min_length_words_list) == 1: 
        return min_length_words_list[0], same_score_dict[min_length_words_list[0]]
    elif len(min_length_words_list) > 1:
        for word in word_list: 
            if word in min_length_words_list:
                return word, same_score_dict[word]
    
    
def get_highest_word_score(word_list):
    """
    Returns winning word. 
    """
    # Initialize dictionary variables for scored words.
    scored_dict = {}
    same_score_dict = {}

    # Score each word in word_list and put into dictionary.
    for word in word_list: 
        score = score_word(word)
        scored_dict[word] = score

    # Identify max value(s)
    all_values = scored_dict.values()
    max_value = max(all_values)
    for word, value in scored_dict.items(): 
        if value == max_value:
            same_score_dict[word] = value

    # Return winning word when tie breaker unneccessary 
    if len(same_score_dict) == 1: 
        for key, value in same_score_dict.items():
            return key, value
    # Initialize tie_breaker function in event of tie
    else: 
        return tie_breaker(same_score_dict, word_list)
