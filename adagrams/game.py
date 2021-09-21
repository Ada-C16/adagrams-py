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

def draw_letters():
    list_letters_pool = ["A", "A", "A", "A", "A", "A", "A", "A", "A",
                    "B", "B",
                    "C", "C",
                    "D", "D", "D", "D",
                    "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
                    "F", "F", 
                    "G", "G", "G", 
                    "H", "H", 
                    "I", "I", "I", "I", "I", "I", "I", "I", "I",
                    "J", 
                    "K", 
                    "L", "L", "L", "L",
                    "M", "M",
                    "N", "N", "N", "N", "N", "N",
                    "O", "O", "O", "O", "O", "O", "O", "O",
                    "P", "P",
                    "Q", 
                    "R", "R", "R", "R", "R", "R", 
                    "S", "S", "S", "S",
                    "T", "T", "T", "T", "T", "T",
                    "U", "U", "U", "U",
                    "V", "V",
                    "W", "W",
                    "X", 
                    "Y", "Y",
                    "Z"]
    list_letters_drawn = []
    for i in range (10):
        random_letter = random.choice(list_letters_pool)
        list_letters_drawn.append(random_letter)
        list_letters_pool.remove(random_letter)
    return list_letters_drawn


    # Alternative Approach to Wave 1   (not yet finished)            
    # random_list_letters = random.choices(list_letters, weights = [9, 2, 2, 4, 12, 2, 3, 2, 9, 
    #                                             1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 
    #                                             2, 2, 1, 2, 1], k = 10)
    # random_dict_letter_occurence = {}

    # for each_letter in random_list_letters:
    #     if each_letter not in random_dict_letter_occurence:
    #         random_dict_letter_occurence[each_letter] = 1
    #     else:
    #         random_dict_letter_occurence[each_letter] += 1
    



def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass


