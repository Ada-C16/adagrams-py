import random

def draw_letters():
    #create a veriable and store letter pool in it
    #store it with a dict. where key is letter and value is how many available

    letter_pool = {
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
    #create a variable and store an empty list for the results that is drawn from the pool
    hand_list = []
    #create a loop to go over items in the letter pool dict. 
    #while loop len list < 10 keep going 
    while len(hand_list) < 10:
        key, value = random.choice(list(letter_pool.items()))
        random_letter = key 
        # if statement to check if the letter is allowed 
        if letter_pool[random_letter] != 0:

            hand_list.append(random_letter)
        # letters are being added to hand list so decrease letter value
            letter_pool[random_letter] -= 1
        else:
            del letter_pool[random_letter]
    return hand_list



def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass