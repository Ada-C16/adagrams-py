
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


def draw_letters():
    """The purpose of draw letters function is to draw 10
    random letters from the letter pool. 
    Returns:
        After looping through the items within the letter pool
        we drew a random sample of 10 letters and appended it to the
        letter list to return our randomly drawn letters.
    """

    letter_list = []

    for letter, frequency in LETTER_POOL.items():
            for i in range(frequency):
                letter_list.append(letter)
    return random.sample(letter_list, 10) # chose to use Random.sample for random sampling without replacement. 
    


def uses_available_letters(word, letter_bank):
    """ The purpose of the uses_available_letters function is
    to check to make sure there are enough letters in the letter 
    bank to be drawn for a word.

    Args:
        word (string): input word
        letter_bank (list): list of drawn letters in a hand. 
        A list that is comprise of 10 strings each representing a 
        letter.

    Returns:
        Boolean: Returns True if every letter in the input word is 
        available in the right quantities in letter bank. It returns false if it 
        does not meet those conditions.
    """    
    letter_frequency = {}

    for letter in letter_bank:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1

    for letter in word:
        if letter not in letter_bank:
            return False
        else:
            letter_frequency[letter] -= 1
            if letter_frequency[letter] < 0:
                return False
    return True


def score_word(word):
    """ The score_word function calculates the points of a given word.
    Each word has a point system and add up for each word. 

    Args:
        word (string): string of characters in each word.

    Returns:
        [integer]: calculates the amount in score_of_points variable.
    """
    score_of_points = 0

    score_chart = {
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

    word = word.upper()

    for letter in word:
        score_of_points += score_chart[letter]
    if len(word) in range(7, 11):
        score_of_points += 8
    return score_of_points


def get_highest_word_score(word_list):
    """ The get_highest_word_score function calculates 
    the word in the list that has the highest score. There
    are exceptions for the word to be a winning word.

    Args:
        word_list (list): list of strings 

    Returns:
        [string]: The string of the winning word is returned.
        [integer]: The score_of_points attached to the word. 
    """    
    winning_word = ""
    highest_score = 0

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            winning_word = word
        elif highest_score == score:
            if len(word) == len(winning_word):
                continue
            elif len(winning_word) == 10:
                continue
            elif len(word) == 10:
                winning_word = word
            elif len(word) < len(winning_word):
                winning_word = word

    return winning_word, highest_score
