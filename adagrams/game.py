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

def convert_letter_dictionary_to_list(letters):
    letter_list = []
    frequency = 0
    
    for key, value in letters.items():
        frequency = value
        for i in range(frequency):
            letter_list.append(key)
    return letter_list

def draw_letters():
    user_hand = []
    principle_letter_list = convert_letter_dictionary_to_list(LETTER_POOL)
    for letter in range(10):
        letter_to_add = principle_letter_list[random.randint(0, len(principle_letter_list)-1)]
        user_hand.append(letter_to_add)
        principle_letter_list.remove(letter_to_add)
    return user_hand

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()

    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    letter_point_dict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
    user_score = 0
    word = word.upper()
    for letter in word:
        user_score += letter_point_dict[letter]
    if len(word) == 7:
        user_score += 8
    elif len(word) == 8:
        user_score += 8
    elif len(word) == 9:
        user_score += 8
    elif len(word) == 10:
        user_score += 8
    return user_score

def convert_word_list_to_list_of_tuples_with_scores(word_list):
    word_score_list = []
    word_score = 0

    for word in word_list:
        word_score = score_word(word)
        word_score_list.append(tuple([word, word_score]))
    return word_score_list

def get_highest_word_score(word_list):
    word_score_list = convert_word_list_to_list_of_tuples_with_scores(word_list)
    max_score = tuple(["", 0])

    for i in range(len(word_score_list)):
        if word_score_list[i][1] == max_score[1]: 
            if len(word_score_list[i][0]) == len(max_score[0]):
                return max_score
            elif len(max_score[0]) == 10:
                return max_score
            elif len(word_score_list[1][0]) == 10:
                max_score = word_score_list[i]
                return max_score
            elif len(word_score_list[i][0]) < len(max_score[0]):
                max_score = word_score_list[i]
                return max_score
            else:
                return max_score
        elif word_score_list[i][1] > max_score[1]:   
            max_score = word_score_list[i]
        else:
            return max_score
    return max_score