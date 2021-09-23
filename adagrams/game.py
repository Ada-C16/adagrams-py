import random

'''
    WAVE 1
'''
def draw_letters():
    letter_pool = letter_dic()
    hand_list = []
    while len(hand_list) < 10:
        key, value = random.choice(list(letter_pool.items()))
        random_letter = key 
        if letter_pool[random_letter] != 0:
            hand_list.append(random_letter)
            letter_pool[random_letter] -= 1
        else:
            del letter_pool[random_letter]
    return hand_list


'''
    WAVE 2
'''
def uses_available_letters(word, letter_bank):
    hand_list = letter_bank[:]
    for letter in word:
        if letter in hand_list:
            hand_list.remove(letter)
            print(hand_list)
        else:
            return False
    print(hand_list)
    return True


'''
    WAVE 3
'''
def score_word(word):
    letters_dict = word_dict()
    score = 0
    for letter in word.upper():
        score += letters_dict[letter]
    if len(word) >= 7:
        score += 8
    return score    


'''
    WAVE 4
'''
def get_highest_word_score(word_list):
    final_word =""
    final_score =0
    tie_list = []
    #for loop
    for word in word_list:
        score = score_word(word)
        if score > final_score:
            final_score = score
            final_word = word 
        elif score == final_score:
            tie_list.append(final_word)
            tie_list.append(word)
            if len(word) == len(final_word):
                final_word = tie_list[0]
            elif len(word) == 10:
                final_score = score 
                final_word = word 
            elif len(final_word) == 10:
                pass
            elif len(word) < len(final_word):
                final_score = score 
                final_word = word

        
    return (final_word, final_score)


'''
    helper functions
'''
def word_dict():
    letters_dict = {}

    for key in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
        letters_dict[key] = 1
    for key in ["D", "G"]:
        letters_dict[key] = 2
    for key in ["B", "C", "M", "P"]:
        letters_dict[key] = 3
    for key in ["F", "H", "V", "W", "Y"]:
        letters_dict[key] = 4
    for key in ["K"]:
        letters_dict[key] = 5
    for key in ["J", "X"]:
        letters_dict[key] = 8
    for key in ["Q", "Z"]:
        letters_dict[key] = 10

    return letters_dict

def letter_dic():
    letter_pool = {
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
    return letter_pool