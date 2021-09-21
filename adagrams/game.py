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

def create_list_of_letters(LETTER_POOL):
    list_of_letters = []
    for letter, count in LETTER_POOL.items():
        while count > 0:
            list_of_letters.append(letter)
            count = count - 1
    return (list_of_letters)

# create_list_of_letters(pool_of_letters)

def draw_letters():
    list_of_letters = create_list_of_letters(LETTER_POOL)
    list_of_random_letters = []
    length_of_list = 10
    while length_of_list > 0: 
        random_index = random.randint(0, (len(list_of_letters)-1))
        list_of_random_letters.append(list_of_letters[random_index])
        list_of_letters.remove(list_of_letters[random_index])
        length_of_list = length_of_list - 1
    return (list_of_random_letters)


def uses_available_letters(word, letter_bank):
    letter_bank = draw_letters()
    print(word) 
    print(letter_bank)
    for letter in word:
        if letter in letter_bank:
            letter_bank.remove(letter)
            return True
        else:
            return False
    



def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass