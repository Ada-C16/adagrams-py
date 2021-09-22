import random
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
def draw_letters():
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

    # for char in word:
    #     if char not in letter_bank_copy:
    #         return False
    #     elif char in letter_bank_copy:
    #         letter_bank_copy.remove(char)
    #     # else:
    #         return True
    # for char in letter_bank:
    # letter_bank_copy=letter_bank
    # for char in word:
    #     if char in letter_bank_copy:
    #         return True
    #         letter_bank_copy.remove(char)
    #     else:
    #         return False
        # for char in word:
        #     if char and word in letter_bank:
        #         return True
        #     else:
        #         return False


    # letter_bank_copy=letter_bank
    # matched_list=[]
    # for char in letter_bank_copy:
    #     for char in word:
    #         if char in letter_bank_copy:
    #             matched_list.append(True)
    #             letter_bank_copy.remove(char)
    #         else:
    #             matched_list.append(False)
    # string_contains_chars = all(matched_list)
    # return string_contains_chars


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass