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

bag_of_letters = []
ten_letters = []

def draw_letters():
    bag_of_letters = []
    ten_letters = []

    for letter in LETTER_POOL:
        value = LETTER_POOL[letter]
        letter_string = letter * value 

        for multiple_letters in letter_string:
            bag_of_letters.append(multiple_letters)

    random.shuffle(bag_of_letters)

    i = 0 
    while i < 10:
        ten_letters.append(bag_of_letters[i])
        i += 1 
    return(ten_letters)



<<<<<<< HEAD
=======



>>>>>>> origin
def uses_available_letters(word, letter_bank):

    bool_count_letters = []
    for char in word:
        if char in letter_bank and word.count(char) <= letter_bank.count(char) :
            bool_count_letters.append(True)
        else:            
            bool_count_letters.append(True)
    if False in bool_count_letters:
        return False
    else:
        return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass