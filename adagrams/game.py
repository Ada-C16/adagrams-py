import random

## WAVE 1 ##
def draw_letters():
    
    letter_pool = []

    letters = ["A", "B", "C", "D", "E",\
         "F", "G", "H", "I", "J",\
               "K", "L", "M", "N", "O",\
                    "P", "Q", "R", "S", "T",\
                         "U", "V", "W", "X", "Y", "Z"]
    weights = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1,]

    for i in range(len(letters)):
        letter = letters[i] 
        frequency = weights[i]
        for j in range(frequency): 
            letter_pool.append(letter)

    result = random.sample(letter_pool, 10)
    
    
    return result



# def draw_letters():
#     import random

#     letter_pool = ["A", "B", "C", "D", "E",\
#          "F", "G", "H", "I", "J",\
#               "K", "L", "M", "N", "O",\
#                    "P", "Q", "R", "S", "T",\
#                         "U", "V", "W", "X", "Y", "Z"]

#     # weights = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1,]


#     for i in range(1):
#         letters = random.sample(letter_pool, weights = (9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1,), k =10)
        
#         return letters
     





##WAVE 2###

def uses_available_letters(word, letter_bank):
    pass


## WAVE 3 ##

SCORE = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}


def score_word(word):

    if len(word) > 6:
        return 8 + sum(SCORE[letter.lower()] for letter in word)
    else:
        return sum(SCORE[letter.lower()] for letter in word)



def get_highest_word_score(word_list):
    pass