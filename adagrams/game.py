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


#


def score_word(word):
    score_chart = {
        1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2 : ["D", "G"],
        3 : ["B", "C", "M", "P"],
        4 : ["F", "H", "V", "W", "Y"],
        5 : ["K"],
        8 : ["J", "X"],
        10: ["Q", "Z"]
    }

def get_highest_word_score(word_list):
    pass