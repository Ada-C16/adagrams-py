import random
def draw_letters():
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

    letter_pool_list = []
    for letter, value in LETTER_POOL.items():
        letter_pool_list += letter * value

    random_numbers = random.sample(range(0, len(letter_pool_list)), 10)
    letter_bank = []
    for x in random_numbers:
        letter_bank.append(letter_pool_list[x])
    print(letter_bank)
    return letter_bank
    
def uses_available_letters(word, letter_bank):
    letter_bank_frequency = {}
    for letter in letter_bank:
        if letter in letter_bank_frequency:
            letter_bank_frequency[letter] += 1
        else:
            letter_bank_frequency[letter] = 1

    character_count = {}
    for letter in word:
        if letter in character_count:
            character_count[letter] += 1
        else:
            character_count[letter] = 1

    for letter, value in character_count.items():
        if letter not in letter_bank_frequency or value > letter_bank_frequency[letter]:
            return False
    return True

def score_word(word):
    SCORE_CHART = {
        1: ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'),
        2: ('D', 'G'),
        3: ('B', 'C', 'M', 'P'),
        4: ('F', 'H', 'V', 'W', 'Y'),
        5: ('K'),
        8: ('J', 'X'),
        10: ('Q', 'Z')
    }
    word = word.upper()
    word_score = 0
    if len(word) in range(7,11):
        word_score += 8

    for letter_score, letters in SCORE_CHART.items():
        for letter in word:
            if letter in letters:
                word_score += letter_score
    return word_score
    
word = 'gfgfgsgf'
score_word(word)

def get_highest_word_score(word_list):
    pass