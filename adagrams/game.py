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
    

##WAVE 2###

def uses_available_letters(word, letter_bank):
    freq = {}
    for elem in letter_bank:
           freq[elem] = letter_bank.count(elem)

    for letter in word:
        # for i in range(len(letter_bank)):
        if letter in letter_bank:
            if letter in freq:
                if freq[letter] == 0:
                    return False
                else:
                    freq[letter] -= 1
        else:
            return False
    return True
        

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


## WAVE 4##
def get_highest_word_score(word_list):
    #wordlist into a dictionary we will use the function from the top that scores the word/
    #use that as a key value 
    
    words_and_scores = {word: score_word(word) for word in word_list}
    #create a high score list using the max function 
    highest_score = max(words_and_scores.values())
    #this next bit of codes finds any ties 
    find_ties = [i for i in words_and_scores.keys()if words_and_scores[i] == highest_score]

    winning_word = find_ties[0]
    for word in find_ties: 
        if len(word) == 10:
            return word, highest_score

        if len(word) < len(winning_word):
            winning_word = word
    return winning_word, highest_score


