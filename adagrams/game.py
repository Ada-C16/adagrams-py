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

    letter_bank = random.sample(letter_pool_list, 10)
  
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

    word_is_valid = True

    for letter, value in character_count.items():
        if letter not in letter_bank_frequency or value > letter_bank_frequency[letter]:
            word_is_valid = False
    return word_is_valid

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

def get_highest_word_score(word_list):
    best_words = []
    best_score = 0
    
    for word in word_list:
        word_score = score_word(word)
        if word_score == best_score:
            best_words.append(word)
        elif word_score > best_score:
            best_words = [word]
            best_score = word_score
    
    best_words_by_length = sorted(best_words, key=len)
    best_length = 0
    if len(best_words_by_length[-1]) == 10:
        best_length = 10
    else:
        best_length = len(best_words_by_length[0])

    for word in best_words:
        if len(word) == best_length:
            return (word, best_score)