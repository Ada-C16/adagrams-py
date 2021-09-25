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
    # use a dictionary with the letter as the key and the number of instances/tiles as the value
    # make a copy of LETTER_POOL (shallow/deep) 
    all_letters = LETTER_POOL.copy()
    # initialize an empty array to hold strings (letters)
    drawn_letters = []
    # continue loop until the list has ten values
    while len(drawn_letters) < 10:
        # random choices takes a weights key that weights probability for each corresponding item
        # in the list being chosen from. Used list of all_letters values to get correct weights
        # especially cool is that as dict values are reduced as letters are drawn, the weights
        # change accordingly, so the probability remains completely accurate
        letter_list = random.choices(list(all_letters), weights=list(all_letters.values()))
        # random choices has to return a list, in this case, list of only one item, but need 
        # to access that one item with [0]
        letter = letter_list[0]
        # if the value associated with the key is greater than 1, append letter to list and 
        # decrease value in dict by 1
        if all_letters[letter] >= 1:
                drawn_letters.append(letter)
                all_letters[letter] -= 1

    return drawn_letters

def score_word(word):
    # change all letters to uppercase to match dict
    word = word.upper()
    # create lists representing points and which letters receive those points
    one_point = ['A','E','I','O', 'U', 'L', 'N','R','S','T']
    two_point = ['D','G']
    three_point = ['B','C','M','P']
    four_point = ['F','H','V','W','Y']
    five_point = ['K']
    eight_point = ['J','X']
    ten_point = ['Q', 'Z']
    # create variable word_score and start at 0
    word_score = 0
    # if word fits these conditions, gets extra points
    if len(word)>=7 and len(word)<11:
        word_score += 8
    # check each letter in word and find which list it is in
    # then assign appropriate amount of points
    for letter in word:
        if letter in one_point:
            word_score += 1
        elif letter in two_point:
            word_score += 2
        elif letter in three_point:
            word_score += 3
        elif letter in four_point:
            word_score += 4
        elif letter in five_point:
            word_score += 5
        elif letter in eight_point:
            word_score += 8
        elif letter in ten_point:
                word_score += 10
    return word_score

def uses_available_letters(word, letter_bank):
    # make a copy of the letter bank
    available_letters = letter_bank.copy()
    # loop through the letters in word and if the letter is in the list, remove it
    # if a letter is not in the list, return False
    for letter in word:
        if letter in available_letters:
            available_letters.remove(letter)
            continue
        else: 
            return False
    return True
    

def get_highest_word_score(word_list):
    # create new dict that will store word as key and score as value
    words_and_scores = {}
    # list will track just scores
    score_list = []
    # populate both list and dict with data from word_list
    for word in word_list:
        score = score_word(word)
        words_and_scores[word] = score
        score_list.append(score)
        
    # find the max score
    max_score = max(score_list)
    # this is list comprehension, loops through dict, if max_score is found as a value, it returns
    # the key, which is a word string. Now have a list of any possible tying words
    words = [k for k, v in words_and_scores.items() if v == max_score]
    # check each word in the tied words list (words) check conditionals and apply results
    for word in words:
        if len(words) == 1:
            return word, max_score
        elif len(word) == 10:
            return word, max_score
    # each final returned pair will be a tuple.  Python automatically converts a comma separated
    # pair of values into a tuple
    else: 
        return min(words, key=len), max_score
    
    
        


        
