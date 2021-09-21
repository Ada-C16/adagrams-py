import random

def draw_letters():
    letters_dict = {'A':9, 'B':2, 'C':2, 'D':4, 'E':12, 'F':2, 'G':3,
        'H':2, 'I':9, 'J':1, 'K':1, 'L':4, 'M':2, 'N':6, 'O':8, 'P':2, 'Q':1,
        'R':6, 'S':4, 'T':6, 'U':4, 'V':2, 'W':2, 'X':1, 'Y':2, "Z":1} 
    
    #for every key in the dictionary, we are multiplying it by its value and adding it to our list
    #when we multiply, we made i a list because we can't multiply strings by integers (for example, we can't multiply 'A' * 9)
    #however we can multiply list of strings by integers (for example, ['a']*9 = ['a','a','a','a', etc])
    #extend is used to then combine that list with the one we created
    letter_list = []
    for i in letters_dict: 
        multiplied = list(i) * letters_dict[i]
        letter_list.extend(multiplied)

    #random.sample is pulling 10 random letters from our list and removing them so we don't pull two Zs or Xs
    #works like pop function but returns random
    ten_letters = random.sample(letter_list, k=10)
    return ten_letters

def uses_available_letters(word, letter_bank):
    # create a copy of the list passed into letter_bank to avoid unwanted side-effects and changing the original list. 
    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy.append(letter)

    # iterate through the string argument passed into the word parameter, and add each letter in the word to a list.
    letters_in_word = []
    for letter in word:
        letters_in_word.append(letter)

    # Create a new list for storing the letters that we will use from the letter bank.
    # Iterate through each letter in letters_in_word list.
        # If a letter from that list is also in the letter bank, we will:
            # 1) Add it to the list of used letter bank letters
            # 2) Remove it from our copy of the letter_bank list
    letter_bank_used = []
    for letter in letters_in_word:
        if letter in letter_bank_copy:
            letter_bank_used.append(letter)
            letter_bank_copy.remove(letter)
    
    # If the length of the argument passed into word is equal to the length of the letter_bank_used list, return True.
    # Otherwise, return false.
    if len(word) == len(letter_bank_used):
        return True
    else:
        return False

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass