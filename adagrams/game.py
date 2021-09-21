def draw_letters():
    pass

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    letter_value_dictionary = {
        'A': 1, 
        'E': 1, 
        'I': 1, 
        'O': 1, 
        'U': 1, 
        'L': 1, 
        'N': 1, 
        'R': 1, 
        'S': 1, 
        'T': 1,
        'D': 2, 
        'G': 2,
        'B': 3, 
        'C': 3, 
        'M': 3, 
        'P': 3,
        'F': 4, 
        'H': 4,
        'V': 4, 
        'W': 4,
        'Y': 4,
        'K': 5,
        'J': 8, 
        'X': 8,
        'Q': 10,
        'Z': 10
    }
    
    sum = 0 
    for letter in word:
        sum += letter_value_dictionary[letter.upper()]

    if len(word) >= 7:
        sum += 8
    
    return sum


def get_highest_word_score(word_list):
    highest_score = score_word(word_list[0])
    winning_word = word_list[0]

    for index in range(1, len(word_list)):
        word = word_list[index]
        this_words_score = score_word(word)
        
        if this_words_score > highest_score:
            highest_score = this_words_score
            winning_word = word
        elif this_words_score == highest_score:
            if len(word) == 10 or len(winning_word) == 10:
                if len(word) == 10 and not len(winning_word) == 10:
                    winning_word = word
            elif len(word) < len(winning_word):
                winning_word = word 

    
    return (winning_word, highest_score)
        


