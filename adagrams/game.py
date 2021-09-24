def draw_letters():
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
    
    letter_list = []
    for letter in LETTER_POOL:
        counter = 0
        while counter < LETTER_POOL[letter]:
            letter_list.append(letter)
            counter += 1
            
    
    random.shuffle(letter_list)
    
    return letter_list[0:10]


def uses_available_letters(word, letter_bank):
    letter_bank_copy = []
    for item in letter_bank:
        letter_bank_copy.append(item)

    for char in word:
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False

    return True



#Iterates through all letters in word to check values of dict
#When found in a value, the key is added to score
#Adds 8 at the end if length of word greater than 6
def score_word(word):
    word = word.upper()
    
    score_chart = {
        1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2 : ["D", "G"],
        3 : ["B", "C", "M", "P"],
        4 : ["F", "H", "V", "W", "Y"],
        5 : ["K"],
        8 : ["J", "X"],
        10: ["Q", "Z"]
    }

    score = 0
    for letter in word:
        for key in score_chart:
            if letter in score_chart.get(key):
                score += key

    if len(word) > 6:
        score += 8

    return score


def get_highest_word_score(word_list):
    words_and_scores = {}
    for word in word_list:
        words_and_scores[word] = score_word(word)

    max_score = max(words_and_scores.values())
    # highest_word = words_and_scores.get(max_score)

    max_score_dict = {}
    for word in words_and_scores:
        if words_and_scores[word] == max_score:
            max_score_dict[word] = len(word)
    
    if len(max_score_dict) == 1:
        for key, value in max_score_dict.items():
            return key, value
        # return max_score_dict.get(max_score), max_score
    # else:
    #     shortest_word = len(max_score_list[0])
    #     for word in max_score_list:
    #         if 


# get_highest_word_score(["AAAAAA", "EEEEEE","IIIIII"])   