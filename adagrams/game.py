def draw_letters():
    # create a data structure for the distribution of letters
    # while len of new data structure - list "letters" is < 10
    #   note to self - double check length of 10 actually means 10
    # use random() to pull a random letter
    #   check if random letter is in our dataset 
    #   check if quantity is > 0
    #    if yes then return letter to list "letters" as single letter strings
    #      qty value of letter decrease by 1
    #    if not - continue 
    pass

def uses_available_letters(word, letter_bank):
    # check if input word uses some or all of the given letters in the hand
    # if a letter in word is in the letter bank
        # remove the letter from a copy of the letter bank 
    # consider how to exit loop (word length)
    # return boolean
        # True if every letter in the word is available
        # false if a letter is not in the list or is not available

    is_letter_in_letter_bank = True
    letters_copy = letter_bank.copy()
    # we have to make a copy of the letter bank because the list is mutable
    #  we don't want to have a side effect of changing the list outside of this function
    word_length = len(word)

    while is_letter_in_letter_bank == True and word_length > 0:
        for letter in word:
            if letter in letters_copy:
                letters_copy.remove(letter)
                word_length -= 1
            else:
                is_letter_in_letter_bank = False
                break
    return is_letter_in_letter_bank

# # ALTERNATE OPTION
#     try:
#         while word_length > 0:
#             for letter in word:
#                 if letter in letters_copy:
#                     letters_copy.remove(letter)
#                     word_length -= 1
#                 else:
#                     raise ValueError
#         return True
#     except ValueError:
#         return False

def score_word(word):
    # return a score (int) of inputted word
    # create score chart data structure
        # dictionary with score int as the key and a list of string letters as the values
    #for each letter in the word
    #   find the letter in the score chart 
        # will need to access the list of letters 
        # for each score value (key)
        #   access the letter which is the value and a list
        #   iteratre thru the list to flag if the letter exists
    # add up the points from each letter in word
    #   define var for total points (count)
    # for letter in word
    #   what is the value of the letter
    #   count values
    # count length of word
    #   if length 7 -10 letters long, add 8 pts
    pass

def get_highest_word_score(word_list):
    pass