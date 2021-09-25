import random

def draw_letters():
    pool_of_letters = {
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

    list_of_letters = list(pool_of_letters.keys())

    draw_ten = []




    for i in range(10):
        random_letter = random.randint(0, 25)
        letter = list_of_letters[random_letter]
        
        while pool_of_letters[letter] == 0:
            random_letter = random.randint(0, 25)
            letter = list_of_letters[random_letter]
        
        draw_ten.append(letter)
        pool_of_letters[letter] -= 1

        
    return draw_ten



def uses_available_letters(word, letter_bank):
    letter_list = letter_bank[:]
    if len(word) > len(letter_list):
        return False
    
    elif len(word) == len(letter_list):
        for letter in word:
            if letter in letter_list:
                letter_list.remove(letter)
        if letter_list is False:
            return True
        else:
            return False
    
    else:
        whole_word = []
        for letter in word:
            if letter not in letter_list:
                return False
            else:
                whole_word.append(letter)
                letter_list.remove(letter)
        if len(whole_word) == len(word):
            return True
        else:
            return False
    


def score_word(word):
    value_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    value_2 = ["D", "G"]
    value_3 = ["B", "C", "M", "P"]
    value_4 = ["F", "H", "V", "W", "Y"]
    value_5 = ["K"]
    value_8 = ["J", "X"]
    value_10 = ["Q", "Z"]

    sum = 0

    if len(word) > 6:
        sum += 8

    for letter in word.upper():
        if letter in value_1:
            sum += 1
        elif letter in value_2:
            sum += 2
        elif letter in value_3:
            sum += 3
        elif letter in value_4:
            sum += 4
        elif letter in value_5:
            sum += 5
        elif letter in value_8:
            sum += 8
        elif letter in value_10:
            sum += 10
    
    return sum



def get_highest_word_score(word_list):
    score_dict = {}
    max_score = 0
    high_score_words = {}

    for word in word_list:
        score_dict[word] = score_word(word)
    
    for score in score_dict.values():
        if score > max_score:
            max_score = score
    
    for word, score in score_dict.items():
        if score == max_score:
            high_score_words[word] = score
        
    shortest_word_length = 10

    for word, score in high_score_words.items():
        if len(word) == 10:
            return word, score
    
        elif len(word) < shortest_word_length:
            shortest_word_length = len(word)
    
    for word, score in high_score_words.items():   
        if len(word) == shortest_word_length:
            return word, score
