import random

POOL_OF_LETTERS = {
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

# Wave 01

"""
The draw_letters function builds a hand of 10 letters
for the user. The letters are randomly drawn from the 
pool of letters.
"""

def draw_letters():
    pool_of_letters = POOL_OF_LETTERS.copy()
    list_of_letters = list(pool_of_letters.keys())

    draw_ten = []

    while len(draw_ten) < 10:
        random_letter = random.randint(0, len(list_of_letters) - 1)
        letter = list_of_letters[random_letter]
        
        if pool_of_letters[letter] == 0:
            continue
        
        draw_ten.append(letter)
        pool_of_letters[letter] -= 1

        
    return draw_ten

# Wave 02 

"""
The use_available_letters function checks to see
whether or not the input word only uses characters 
that are contained within a collection (or hand) 
of drawn letters.
"""

def uses_available_letters(word, letter_bank):
    letter_list = letter_bank[:]
    letter_map = {}

    if len(word) > len(letter_list):
        return False
    
    whole_word = []
    for letter in letter_list:
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1

    for letter in word:
        if letter not in letter_map.keys() or letter_map[letter] == 0:
            return False
        
        whole_word.append(letter)
        letter_map[letter] -= 1

    return len(whole_word) == len(word)

# Wave 03

"""
The score_word function returns the score of a given word as
defined by the Adagrams game.
"""

def score_word(word):
    score_map = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, 
        "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
        "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, 
        "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, 
        "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, 
        "Z": 10
    }

    LONG_WORD_BONUS = 8
    LONG_WORD_BONUS_LENGTH = 7
    BASIC_SCORE = 0

    score = LONG_WORD_BONUS if len(word) >= LONG_WORD_BONUS_LENGTH else BASIC_SCORE

    for letter in word.upper():
        if letter in score_map:
            score += score_map[letter]
    
    return score

# Wave 04

"""
The get_highest_word_score function checks for the
highest scored word that the user has submitted.
"""

def get_highest_word_score(word_list):
    score_dict = {}
    max_score = 0

    for word in word_list:
        score_dict[word] = score_word(word)
    
    max_score = max(score_dict.values())
    shortest_word_length = 10
    shortest_word = None

    for word, score in score_dict.items():
        if score == max_score:
            if len(word) == 10:
                return word, score
            elif len(word) < shortest_word_length:
                shortest_word_length = len(word)
                shortest_word = word
    
    return shortest_word, max_score