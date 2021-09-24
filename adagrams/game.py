import random

def draw_letters(): # Time complexity: O(1)  Space complexity: O(1)
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
        list_letters_pool.remove(random_letter)  # remove the drawn letter from the original list of letter pool after each random draw
    return list_letters_drawn

def uses_available_letters(word, letter_bank):  # Time complexity: O(2n)  Space complexity: O(n)
    # This portion of function is to count the frequency of each letter drawn and store it in dict
    letter_bank_dict = {}
    for each_letter in letter_bank:
        if each_letter not in letter_bank_dict:
            letter_bank_dict[each_letter] = 1
        else:
            letter_bank_dict[each_letter] += 1
    
    # This portion of function is to split each char in the word and count the 
    # frequency of each char. 
    # If the char is in the dictionary and its count is not over the its 
    # corresponding count of being drawn.
    # The loop will skip and continue to check the next char. Once there is a 
    # char does not fit any of these two conditions, it will return False. 
    for each_char in word:
        char_count = word.count(each_char)
        if each_char in letter_bank_dict and char_count <= \
        letter_bank_dict[each_char]:
            continue
        else:    
            return False
    return True

def score_word(word):  # Time complexity: O(n)  Space complexity: O(1)
    dict_score_chart = {
                        "A" : 1,
                        "E" : 1,
                        "I" : 1,
                        "O" : 1,
                        "U" : 1,
                        "L" : 1,
                        "N" : 1,
                        "R" : 1,
                        "S" : 1,
                        "T" : 1,
                        "D" : 2,
                        "G" : 2,
                        "B" : 3,
                        "C" : 3,
                        "M" : 3,
                        "P" : 3,
                        "F" : 4,
                        "H" : 4,
                        "V" : 4,
                        "W" : 4,
                        "Y" : 4,
                        "K" : 5,
                        "J" : 8,
                        "X" : 8,
                        "Q" : 10,
                        "Z" : 10,
                    }
    score = 0 
    for each_char in word.upper():  # unify the case of each char
        if each_char in dict_score_chart:
            score += dict_score_chart[each_char]
    if len(word) >= 7:      # add additional score if length over 7
        score += 8
    return score

def get_highest_word_score(word_list): 
    # calculate the score of each word in the list and put them in word-score pair to dict
    dict_word_score = {}
    for each_word in word_list:                                                     
        dict_word_score[each_word] = score_word(each_word)
    
    # find out the max score by looping through the values of dict
    max_score = max([each_word_score for each_word_score in dict_word_score.values()]) 

    # looping through the keys(words) of the dict, compare if its value equals max_score, 
    # append the key(word) to an empty if it is True
    list_word_with_max_score = [word for word in dict_word_score.keys()if 
                                dict_word_score[word] == max_score]
        
    max_length = max([len(each_word)for each_word in list_word_with_max_score])

    # if max_length > 10, it loops through the keys(words) of the dict, compare if its length equals max_length, 
    # if it does, return a tuple (each_word, max_score)
    if max_length >= 10:
        for each_word in dict_word_score.keys():
            if len(each_word) == max_length:
                return (each_word, max_score) 
    else:
        # if max_length < 10, it finds out the min length. It loops through the keys(words) of the dict, compare if its length equals min_length, 
        # if it does, return a tuple (each_word, max_score)
        min_length = min([len(each_word)for each_word in list_word_with_max_score])

        for each_word in dict_word_score.keys():
            if len(each_word) == min_length:
                return (each_word, max_score) 








