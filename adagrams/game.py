import random

def dictionary_to_list(dict):
    letter_list = []
    for key, value in dict.items():
        for i in range(value): 
            letter_list.append(key)
    
    return letter_list

def draw_letters():
    letter_pool = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1,
    }

    possible_letters = dictionary_to_list(letter_pool)

    player_hand = random.sample(possible_letters, 10)
    return player_hand

def uses_available_letters(word, letter_bank):
    letter_dict = dict()

    for letter in letter_bank:
        if letter in letter_dict:              
            letter_dict[letter] +=1
        else:
            letter_dict[letter] = 1

# if rue if every letter in input word is available in the right quanities 
#  if letter in word not in player hand,  or has too much of(letter) compared to letter bank
    # return false
    # 
    for letter in word:
        if letter not in letter_bank:
            return False
        else:
            letter_dict[letter] -= 1
            if letter_dict[letter] < 0:
                return False
    return True
    


def score_word(word):
    
    player_score = 0
    # make a score chart
    score_chart =  {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2,
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10,
    }
    word = word.upper()

    for letter in word:
        player_score += score_chart[letter]
    if len(word) in range(7, 11):
        player_score += 8
    return player_score
    # at each letter, it sums the value of each letter
    # total score = sum of all letter values
    # if len(word) = 7,8,9,10, score gets 8 additional points  
def get_highest_word_score(word_list):
    # for word in word_list
    #  score each word by using score_word
    # store the score info about each word in a tuple

    # if a score is = to each other
    # winner = the word with fewer letters
    # EXCEPT if the lnegth of word is 10, then if it his the highest and length of 10 it is the winner
    #  if scores in tow words = and length of 2 words =, then whichever comes first