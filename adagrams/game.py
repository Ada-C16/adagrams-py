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

    #create a letter_pool and store an empty list for the results that is drawn from the pool
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
        #delete letter_pool[random_letter]
            del letter_pool[random_letter]
    return hand_list



def uses_available_letters(word, letter_bank):
    hand_list = letter_bank[:]
    # check if the letter in hand_list is in a word 
    for letter in word:
        if letter in hand_list:
        #if is a  word return True
            hand_list.remove(letter)
            print(hand_list)
        else:
            return False
    print(hand_list)
    return True



def score_word(word):
#save letters in a dic with respective value 
    letters_dict = {}
    for key in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
        letters_dict[key] = 1
    for key in ["D", "G"]:
        letters_dict[key] = 2
    for key in ["B", "C", "M", "P"]:
        letters_dict[key] = 3
    for key in ["F", "H", "V", "W", "Y"]:
        letters_dict[key] = 4
    for key in ["K"]:
        letters_dict[key] = 5
    for key in ["J", "X"]:
        letters_dict[key] = 8
    for key in ["Q", "Z"]:
        letters_dict[key] = 10
#crete loop to run through the word
    score = 0
    for letter in word.upper():
        score += letters_dict[letter]
    if len(word) >= 7:
        score += 8
    return score    

def get_highest_word_score(word_list):
    pass