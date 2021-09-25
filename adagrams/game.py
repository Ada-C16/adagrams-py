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

SCORE_CHART = {
    1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'],
    2: ['d', 'g'],
    3: ['b', 'c', 'm', 'p'],
    4: ['f', 'h', 'v', 'w', 'y'],
    5: ['k'],
    8: ['j', 'x'],
    10: ['q', 'z'],
}


def draw_letters():
    letter_hand = []
    letter_pool_list = []
    for letter, number in LETTER_POOL.items():
        letter_pool_list.extend([letter] * number)
    for i in range(10):
        letter = random.choice(letter_pool_list)
        letter_hand.append(letter)
        letter_pool_list.remove(letter)
    return letter_hand


def uses_available_letters(word, letter_bank):
    word_checker = letter_bank.copy()
    for char in word:
        if char not in word_checker:
            return False
        else:
            word_checker.remove(char)
    return True


def score_word(word):
    word = word.lower()
    num_points = 0
    for char in word:
        for score, letters in SCORE_CHART.items():
            if char in letters:
                num_points += score
    if len(word) >= 7:
        num_points += 8
    return num_points


def get_highest_word_score(word_list):
    #returns tuple with the highest scored word, and the score
    #find the scores for each word in word list
    #find the highest score

    words_and_scores = []

    for word in word_list:
        score = score_word(word)
        words_and_scores.append((word, score))

    highest_score = 0
    for pair in words_and_scores:
        if pair[1] > highest_score:
            highest_score = pair[1]
    
    high_score_words = []
    for pair in words_and_scores:
        if pair[1] == highest_score:
            high_score_words.append(pair)

    if len(high_score_words) > 1:
        for pair in high_score_words:
            if len(pair[0]) == 10:
                return pair
            else:
                shortest_length = 10
                for pair in high_score_words:
                    if len(pair[0] < shortest_length):
                        shortest_length = len(pair[0])
                
                for pair in high_score_words:
                    if len(pair[0]) == shortest_length:
                        return pair




# get_highest_word_score(["X", "XXx", "XXX", "XXX"])  

