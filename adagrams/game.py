def draw_letters():
    
    pass

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):

    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10}

    if len(word) == 0:
        return 0
    elif len(word) > 0:
        lower_word = word.lower()
        total_score = 0
        if len(lower_word) in range (7,11):
                total_score += 8
        for letter in lower_word:
            total_score += score[letter]
            
    return total_score


def get_highest_word_score(word_list):

    pass