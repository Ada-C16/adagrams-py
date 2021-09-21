import random 

LETTER_POOL = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 
    'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 
    'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1}

SCORE_CHART = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T") : 1,
    ("D", "G") : 2,
    ("B", "C", "M", "P") : 3,
    ("F", "H", "V", "W", "Y") : 4,
    ("K") : 5,
    ("J", "X") : 8,
    ("Q", "Z") : 10,
}


# Wave 1
def draw_letters():
    """
    Takes in no parameters,
    returns an array of random 10 strings from LETTER_POOL
    """
    letters = []
    letter_count = LETTER_POOL.copy()  # could also be letter_bank, but not sure yet
    i = 0
    while len(letters) < 10:
        random_letter = random.choice(list(LETTER_POOL))
        if letter_count[random_letter] > 0:
            letter_count[random_letter] -= 1
            letters.append(random_letter)
        if letter_count[random_letter] < 0:
            letters.remove(random_letter)
        i += 1
    return letters


# Wave 2
def uses_available_letters(word, letter_bank):
    """
    Takes in two parameters: word, letter_bank,
    returns True if every letter in word is available,
    otherwise returns False.
    """
    pass
    # word: str, describes input word
    # letter_bank: letters list from draw_letters()
    # returns True or False
        # True: if every letter is available in letter_bank
        # False: letter not in letter_bank, too much compared to letter_bank


# Wave 3        
def score_word(word):
    """
    Takes one parameter word, 
    returns integer total_score of string word
    """
    pass
    # word: str of characters
    # returns integer representing points
    # each letter in word has a point value
    # number of points of each letter is summed, total_score of word
    # if len(word) >= 7 or len(word) <= 10, word +8 points


# Wave 4
def get_highest_word_score(word_list):
    """
    Takes one parameter word_list to find the highest scoring word,
    returns the winning word in a tuple: (winning_word, top_score)
    """
    pass
    # word_list: list of strings
    # tie-breaking rules:
        # prefer word with fewest letters
        # if top_score is btwn multiple words
            # word with len() == 10 is winning_word
        # if multiple words have same total_score, same len()
            # store these in a tie_list
            # winning_word == tie_list[0]