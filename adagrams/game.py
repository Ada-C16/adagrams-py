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
    letters_left = LETTER_POOL.copy() #initializing local variable as copy of LETTER_POOL so it can be manipulated
    choice_ten = [] #initializing empty list to hold randomly chosen letters
    while len(choice_ten) < 10: #the final loop will result in 10 letters in the list
        letter = random.choice(list(letters_left)) #randomly choosing letter from dictionary
        if letters_left[letter] > 0: # making sure there are still letters in the bag
            choice_ten.append(letter) #adding chosen letter to list
            letters_left[letter] -= 1 #short hand to say variable is now equal to variable minus one 
                                      # ex: letters_left[letter] = letters_left[letter] - 1
    return choice_ten
    # print(choice_ten)
    # print(letters_left)
        
        

def uses_available_letters(word, choice_ten):
    letters_in_hand = choice_ten.copy()
    for letter in word:
        if letter in letters_in_hand:
            letters_in_hand.remove(letter)
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass