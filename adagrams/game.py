# from tests.test_wave_01 import LETTER_POOL
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
    letter_pool_list = list(LETTER_POOL.keys())
    letter_strings = []
    letter_freq = {}

    while len(letter_strings) < 10:
        
        letter = random.choice(letter_pool_list)

        count_in_letter_freq = 0
        # count_in_letter_freq is the value of letter_freq
        if letter in letter_freq:
            count_in_letter_freq = letter_freq[letter]
        #count_in_letter_pool is the value of LETTER_POOL
        count_in_letter_pool = LETTER_POOL[letter]
        
        if count_in_letter_freq < count_in_letter_pool:
            letter_strings.append(letter)
            if letter in letter_freq:
                letter_freq[letter]+=1
            else:
                letter_freq[letter] = 1

    return letter_strings

        


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]
    word_list = []
    for letter in word:
        if letter in letter_bank_copy:
            # Todo it in more time efficient way
            letter_bank_copy.remove(letter)
            word_list.append(letter)
            # check if all the letters in word is in word_list
            if len(word) == len(word_list):
                return True
            
        else : 
            return False



def score_word(word):
    score = {
        "a": 1,
        "b": 3,
        "c": 3,
        "d": 2,
        "e": 1,
        "f": 4,
        "g": 2,
        "h": 4,
        "i": 1,
        "j": 8,
        "k": 5,
        "l": 1,
        "m": 3,
        "n": 1,
        "o": 1,
        "p": 3,
        "q": 10,
        "s": 1,
        "t": 1,
        "u": 1,
        "v": 4,
        "w": 4,
        "x": 8,
        "y": 4,
        "z": 10 }
    if len(word) == 0:
        return 0
    elif len(word)> 0:
        lower_word = word.lower()
        total_score = 0
        if len(lower_word) in range(7,11):
            total_score += 8
        for letter in lower_word:
            total_score += score[letter]
            
    return total_score




def get_highest_word_score(word_list):
    # create an empty dict to store key and value for each word in the word_list
    word_dict = {}
    max_score_list = []
    tied_words = []

    for word in word_list:
        #calling score_word function to get the score for each word
        word_score = score_word(word)
        #put the word_score as a value for each word
        word_dict[word] = word_score
        # get the key that has max value in word_dict
        max_score = max(word_dict, key= word_dict.get)
        max_score_value = word_dict[max_score]

    # create a list to have the key as a first index and value as a second index    
    max_score_list.append(max_score)
    max_score_list.append(max_score_value)
    for key,value in word_dict.items():
        if value == max_score_value:
            tied_words.append(key)
    if len(tied_words) == 1:
        return (tied_words[0],max_score_value)
    else:
        for word in tied_words:
            if len(word) == 10:
                return (word,max_score_value)
        fewer_letters = min(tied_words, key= len)
        return(fewer_letters, max_score_value)    
