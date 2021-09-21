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

LETTER_SCORE = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def draw_letters():
    # initialize list of letters
    chosen_letters = []
    remaining_letters_count = 0
    for letter, count in LETTER_POOL.items():
        remaining_letters_count += count
    if remaining_letters_count >= 10:
    # do this 10 times:
        while len(chosen_letters) != 10:
            # from letter bank select random letter
            drawn_letter = key, value = random.choice(list(LETTER_POOL.items()))
            # check value of letter is not zero
            if LETTER_POOL[drawn_letter[0]] != 0:
                # add letter to list
                chosen_letters.append(drawn_letter[0])
                # if chosen, decrease value by 1
                LETTER_POOL[drawn_letter[0]] -= 1
    return chosen_letters

def uses_available_letters(word, letter_bank):
    # checks to make sure that word is composed of elements in letter_bank
    word = word.upper()
    letter_bank_copy = letter_bank[:]
    if isinstance(word, str) and len(word) <= 10:
        for char in word:
            if char in letter_bank_copy:
                letter_bank_copy.remove(char)
            else:
                return False
        return True
    return False
    # make a copy of letter_bank    
    # ensure word is a string of 10 or less char
    # loop through the word char by char
    # if in letter_bank copy, proceed - if not in letter bank copy, return false
    # (loop through original list, but as we loop, we check the copy)
    # remove char from letter_bank copy
    # return True

def score_word(word):
    #inputs user input (word) returns score
    total_word_score=0
    word = word.upper()
    for char in word:
        total_word_score += LETTER_SCORE[char]
    if len(word) >=7:
        total_word_score += 8
    return total_word_score

    #initialize total word score = 0
    #iterate through word
    #for each letter, access in dictionary
    #add value to total word score
    #if word length is >=7, add 8 points

def get_highest_word_score(word_list):
    #inputs list of words
    #returns a tuple of highest scoring word + highest score

    #initialize max value to 0
    max_value = 0
    words_score = []
    for word in word_list:
        score=score_word(word)
        words_score.append((word,score))
        if score > max_value:
            max_value=score
    max_score_words=[]
    for word_info in words_score:
        if word_info[1] == max_value:
            max_score_words.append((word_info[0],word_info[1],len(word_info[0])))
    if len(max_score_words) > 1:
        min_length=10
        for word_info in max_score_words:
            if word_info[2] == 10:
                return word_info[0],word_info[1]
            if word_info[2] < min_length:
                min_length = word_info[2]
        for word_info in max_score_words:
            if word_info[2] == min_length:
                return word_info[0],word_info[1]
    else:
        return(max_score_words[0][0],max_score_words[0][1])

#print(get_highest_word_score(["hello","ada","academy"]))

    #initialize empty list (high_score_words[])
    #iterate through word_list with score_word
        ##find max value
    #iterate through word_list again and store words with max_value to high_score_words[]
    #if word is 10 characters, return tuple
    #else, if word length is < word length of other words, return tuple
    #else, return tuple of first word