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

SCORE_LIST = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T" ],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
    }


"""
Create_list_of_letters function returns a list of all letters in. 
Based on letter_pool there are total 98 letters in the list. 
"""
def create_list_of_letters(LETTER_POOL):
    list_of_letters = []
    for letter, count in LETTER_POOL.items():
        while count > 0:
            list_of_letters.append(letter)
            count = count - 1
    return (list_of_letters)


"""
 draw_letters function returns a list of random 10 letters 
 from create_list_of_letters function.  

"""
def draw_letters():
    list_of_letters = create_list_of_letters(LETTER_POOL)
    list_of_random_letters = []
    length_of_list = 10
    while length_of_list > 0: 
        random_index = random.randint(0, (len(list_of_letters)-1))
        list_of_random_letters.append(list_of_letters[random_index])
        list_of_letters.remove(list_of_letters[random_index])
        length_of_list = length_of_list - 1
    return (list_of_random_letters)


"""
 uses_available_letters returns true if every letter in the word is available in the letter bank.
returns false if not.  

"""
def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]
    condition = None
    while len(word) > 0:
        for letter in word:
            if letter in letter_bank_copy:
                letter_bank_copy.remove(letter)
                condition = True
                word = word.replace(letter,"")
            else:
                return False
    return condition
    
"""
score_word function returns the total points for the word based on score chart.
"""
def score_word(word): 
    total_score = 0
    if len(word) >= 7:
            total_score += 8
    for score, letters in SCORE_LIST.items():
        for letter in word.upper():
            if letter in letters:
                    total_score += score
    return total_score

"""
get_word_score function retuns dictionary of scores, where letter is a key and the score is a value.

"""
def get_words_score(word_list):
    dic_of_scores = {}
    for index in range(len(word_list)):
        word_score = score_word(word_list[index])
        dic_of_scores[word_list[index]] = word_score
    print(dic_of_scores)
    return dic_of_scores
    
"""
get_highest_score function retturns list of highest scores (integer)
based on get_words_score function. 
"""
def get_highest_score(word_list):
    list_of_highest_scores = []
    dic_of_scores = get_words_score(word_list)
    scores_list = list(dic_of_scores.values())
    print(scores_list)
    highest = scores_list[0]

    for index in range(len(scores_list)):
        if scores_list[index] > highest:
            highest = scores_list[index]

    for index in range(len(scores_list)):
        if highest == scores_list[index]:
            list_of_highest_scores.append(highest)
    return list_of_highest_scores


"""
get_highest_word_score function retuns a tuple with a word as a first element, 
and the highest score as a second element. 
"""
def get_highest_word_score(word_list):
    list_of_words = []
    list_of_highest_scores = get_highest_score(word_list)
    dic_of_scores = get_words_score(word_list)

    if len(list_of_highest_scores) <= 1:
        for word, score in dic_of_scores.items():
            if score in list_of_highest_scores:
                winner =(word, score)
    else: 
        for word, score in dic_of_scores.items():
            if score in list_of_highest_scores:
                list_of_words.append(word)

        winner = (list_of_words[0], score)
        min_length = len(list_of_words[0])

        for index in range(len(list_of_words)):
            if len(list_of_words[index]) == 10:
                winner =(list_of_words[index], score)
                return winner

            elif len(list_of_words[index]) < min_length:
                min_length = len(list_of_words[index])
                winner =(list_of_words[index], score)
                
    return (winner)        

