import random
# from tests.test_wave_01 import LETTER_POOL

def draw_letters():
    letter_bank = {'A':9, 'B':2, 'C':2, 'D': 4, 'E': 12, 'F': 2, 'G':3, 'H': 2, 'I': 9, 'J': 1, 'K':1, 'L':4, 'M': 2, 'N':6, 'O': 8, 'P':2, 'Q':1, 'R': 6, 'S': 4, 'T':6, 'U':4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z':1}
    tile_bag = []
    for k, v in letter_bank.items():
        for each_letter in range(v):
            tile_bag.append(k)

    tile_list = []
    for ten_letters in range(10):
        letter = random.choice(tile_bag)
        tile_list.append(letter)
        tile_bag.remove(letter)

    return tile_list
   

def uses_available_letters(word, letter_bank):
    letter_list = [letter for letter in letter_bank if letter in word]
    if len(letter_list) == len(word):
        return True
    return False

    # let_list =[]
    # for letter in letter_bank:
    #     if letter in word:
    #         n = letter_bank[letter_bank.index(letter)]
    #         let_list.append(n)
    #         if len(let_list) == len(word):
    #             return True
    # return False



    # freq_dict={}
    # counter_word={}

    

    # for one_letter in word:
    #     if one_letter not in letter_bank:
    #         return False
    #     else:
    #         if one_letter in counter_word:
    #             counter_word[one_letter] += 1
    #         else:
    #             counter_word[one_letter] = 1
    # for letter in letter_bank:
    #     if letter in freq_dict:
    #         freq_dict[letter]+=1
    #     else:
    #         freq_dict[letter]=1
    # if freq_dict[one_letter]>= counter_word[one_letter]:
    #    one_letter=True
    # else:
    #     one_letter=False
    # return one_letter


    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass