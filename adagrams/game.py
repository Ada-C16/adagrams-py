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

def convert_letter_dictionary_to_list(letters):
    """
    Converts the letter, frequency dictionary to a principle list
    """
    letter_list = []
    for letter, frequency in letters.items():
        for i in range(frequency):
            letter_list.append(letter)
    return letter_list

def draw_letters():
    """
    Draws random letters from letter frequency list to populate a user hand
    """
    user_hand = []
    principle_letter_list = convert_letter_dictionary_to_list(LETTER_POOL)
    for letter in range(10):
        letter_to_add = principle_letter_list[random.randint(0, len(principle_letter_list)-1)]
        user_hand.append(letter_to_add)
        principle_letter_list.remove(letter_to_add)
    return user_hand

def uses_available_letters(word, letter_bank):
    """
    Checks that word user guessed word only utilizes correct number of letters and letters from user hand
    """
    letter_bank_copy = letter_bank.copy()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    """
    Scores user guessed word based on individual letter point value, with a bonus for words 7-10 letters
    """
    letter_point_dict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
    user_score = 0
    word = word.upper()
    for letter in word:
        user_score += letter_point_dict[letter]
    if len(word) > 6 and len(word) < 11:
        user_score += 8
    return user_score

def convert_word_list_to_list_of_tuples_with_scores(word_list):
    """
    Takes a list of words, evaluates the points for each word, puts word and point value in a tuple
    appends tuple to a principle list of words and scores
    """
    word_score_list = []
    word_score = 0
    for word in word_list:
        word_score = score_word(word)
        word_score_list.append(tuple([word, word_score]))
    return word_score_list

def get_highest_word_score(word_list):
    """
    Looks at user words and returns highest scoring word
    """
    word_score_list = convert_word_list_to_list_of_tuples_with_scores(word_list)
    max_score = tuple(["", 0])
    for i in range(len(word_score_list)):
        if word_score_list[i][1] == max_score[1]:  #if the word score being evaluated is tied with current max score
            if len(word_score_list[i][0]) == len(max_score[0]): #if the length of the word is same length as max score
                return max_score #"return first one supplied"
            elif len(max_score[0]) == 10: #prefer current max scoring word if length equals 10
                return max_score 
            elif len(word_score_list[1][0]) == 10: #prefer evaluated word score if length equals 10
                max_score = word_score_list[i]
                return max_score
            elif len(word_score_list[i][0]) < len(max_score[0]): #prefer word that is less length overall
                max_score = word_score_list[i]
                return max_score
            else:
                return max_score
        elif word_score_list[i][1] > max_score[1]: #prefer evaluated word score worth more points
            max_score = word_score_list[i]
        else:
            return max_score
    return max_score