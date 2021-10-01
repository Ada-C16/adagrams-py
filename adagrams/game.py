import random

'''
    WAVE 1 - function returns an array of ten random letters
'''
def draw_letters():
    letter_pool = letter_dict()
    hand_list = []
    while len(hand_list) < 10:
        key = random.choice(list(letter_pool.keys()))
        random_letter = key 
        if letter_pool[random_letter] != 0:
            hand_list.append(random_letter)
            letter_pool[random_letter] -= 1      
        del letter_pool[random_letter]
    return hand_list


'''
    WAVE 2 - function checks if an input word is within the hand of letters and 
    returns a boolean value
'''
def uses_available_letters(word, letter_bank):
    hand_list = letter_bank[:]
    for letter in word:
        if letter in hand_list:
            hand_list.remove(letter)
        else:
            return False
    return True


'''
    WAVE 3 - function returns the score of a given word
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
    WAVE 4 - function checks which word has the highest score 
    and returns a tuple that contains the highest vaue and its
    respective word
'''
def get_highest_word_score(word_list):
    word_highest_score =""
    highest_score =0
    #for loop
    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            word_highest_score = word 
        elif score == highest_score:
            if len(word) == 10 and len(word_highest_score) != 10:
                highest_score = score 
                word_highest_score = word
            elif len(word) < len(word_highest_score) and len(word_highest_score) < 10:
                highest_score = score 
                word_highest_score = word
            # word_highest_score = word

    return (word_highest_score, highest_score)


'''
    helper function stores and returns a dictionary - each letter within the
    dictionary has a point value. 
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

'''
    helper function stores and returns a dictionary. 
'''

def letter_dict():
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