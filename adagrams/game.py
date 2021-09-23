import random

def draw_letters():
    LETTER_POOL = {
        'A': 5, 
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

    LETTER_POOL_LIST = []  
    for letter in LETTER_POOL.keys():
        for count in range(LETTER_POOL[letter]):
            LETTER_POOL_LIST.append(letter)
    
    letters = []
    while len(letters) < 10:
        letter = random.choice(LETTER_POOL_LIST)
        letters.append(letter)
        LETTER_POOL_LIST.remove(letter)
    return letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]
    matched_list=[]
    for letter in word:
        if letter in letter_bank_copy:
            matched_list.append(True)
            letter_bank_copy.remove(letter)
        else:
            matched_list.append(False)
    string_contains_chars = all(matched_list)
    return string_contains_chars

def score_word(word):
    score_chart = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 
        2: ['D','G'], 
        3: ['B', 'C', 'M', 'P'], 
        4: ['F', 'H', 'V', 'W', 'Y'], 
        5: ['K'], 
        8: ['J','X'], 
        10: ['Q','Z'] 
    }

    new_word = word.upper()
    points = 0
    if len(new_word) >= 7:
        points += 8
    for char in new_word:
        for point, letter_list in score_chart.items():
            if char in letter_list:
                points += point     
    return points

def get_highest_word_score(word_list):
    scores = []
    for word in word_list:
        score = score_word(word)
        scores.append(score)
        zipped_lists = zip(word_list, scores)
        word_scores = list(zipped_lists)
        
    highest_score = 0
    fewest_letters = 10
    tie_breaker = []

    for word, score in word_scores:
        if score >= highest_score:
            highest_score = score

    for word, score in word_scores:
        if highest_score == score:
            tie_breaker.append((word, score))

    for word, score in tie_breaker:
        if len(word) >= 10:
            return ((word, score))
        if len(word) < fewest_letters:
            fewest_letters = len(word)
            return((word, score))