def draw_letters():

    import random

    main_letters_list = ["a", "a", "a", "a", "a", "a", "a", "a","a", "b", "b", "c", "c", "d", "d", "d", "d", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "f", "f", "g", "g", "g", "h", "h", "i", "i", "i", "i", "i", "i", "i", "i", "i", "j", "k", "l", "l", "l", "l", "m", "m", "n", "n", "n", "n", "n", "n", "o", "o", "o", "o", "o", "o", "o", "o", "p", "p", "q", "r", "r", "r", "r", "r", "r", "s", "s", "s", "s", "t", "t", "t", "t", "t", "t", "u", "u", "u", "u", "v", "v", "w", "w", "x", "y", "y", "z"]  

    main_letters_list_copy = []
    user_hand = []

    for letter in main_letters_list:
        main_letters_list_copy.append(letter)

    i = 0
    while i < 10:
        letter = random.choice(main_letters_list_copy)
        user_hand.append(letter.capitalize())
        main_letters_list_copy.remove(letter)
        i += 1

    return user_hand

def uses_available_letters(word, letter_bank):

    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy.append(letter)
    
    for letter in word:
        if letter not in letter_bank_copy:
            return False
        elif letter in letter_bank_copy:
            letter_bank_copy.remove(letter)

    return True
    

def score_word(word):
    score_chart = { 
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 
        2: ["D", "G"], 
        3: [ "B", "C", "M", "P"], 
        4: ["F", "H", "V", "W", "Y"], 
        5: ["K"], 
        8 : ["J", "X"], 
        10: [ "Q", "Z"] 
        }
        
    word = word.upper()
    score = 0
    for letter in word:
        for key, value in score_chart.items():
            if letter in value:
                score += key
    
    if len(word) >= 7:
        score += 8

    return score
   

def get_highest_word_score(word_list):
    highest_score_word_list = []
    comparing_word_scores = {}
    current_word_score = 0
    for word in word_list:
        current_word_score = score_word(word)
        if comparing_word_scores.get(current_word_score):
            comparing_word_scores[current_word_score].append(word)
        else:
            comparing_word_scores[current_word_score] = []
            comparing_word_scores[current_word_score].append(word)

    current_highest_score=0 
    for score, words in comparing_word_scores.items():
        if score > current_highest_score:
            highest_score_word_list.clear()
            for word in words:
                highest_score_word_list.append(word)
            current_highest_score = score
    
    shortest_word_length = 10
    shortest_word_list = []
    if len(highest_score_word_list) == 1:
        final_tuple = (highest_score_word_list[0], current_highest_score)
        return final_tuple
    elif len(highest_score_word_list) > 1:
        for word in highest_score_word_list:
            if len(word) == 10:
                return (word, current_highest_score)
            else:
                if len(word) < shortest_word_length:
                    shortest_word_list.append(word)
                    shortest_word_length=len(word)
        
        return (shortest_word_list[-1], current_highest_score)
         
  