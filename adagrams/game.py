import random
LETTER_POOL = ["A", "A", "A", "A", "A", "A", "A", "A", "A", 
"B", "B", 
"C", "C", 
"D", "D", "D", "D", 
"E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
"F", "F", 
"G", "G", "G", 
"H", "H", 
"I", "I", "I", "I", "I", "I", "I", "I", "I", 
"J", 
"K", 
"L", "L", "L", "L", 
"M", "M",
"N", "N", "N", "N", "N", "N",
"O", "O", "O", "O", "O", "O", "O", "O",
"P", "P",
"Q",
"R", "R", "R", "R", "R", "R",
"S", "S", "S", "S",
"T", "T", "T", "T", "T", "T",
"U", "U", "U", "U",
"V", "V",
"W", "W",
"X",
"Y", "Y",
"Z"]

SCORE_CHART = {
    "A": 1,
    "E": 1,
    "I": 1,
    "O": 1,
    "U": 1,
    "L": 1,
    "N": 1,
    "R": 1,
    "S": 1,
    "T": 1,
    "D": 2,
    "G": 2,
    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,
    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10
}

def draw_letters():
    is_freq_correct = False
    #Loop to check if letter frequency is correct in relation to LETTER_POOL
    while is_freq_correct == False:
        letter_bank = random.choices(LETTER_POOL, k=10)
        # random.choices() documentation at https://docs.python.org/3/library/random.html
        is_freq_correct = True
        #Begin with assuming frequency is correct
        #print(letter_bank)
        for letter in letter_bank:
            if letter_bank.count(letter) > LETTER_POOL.count(letter):
                is_freq_correct = False
                #Letter frequency is incorrect. Breaks the loop and creates new hand of letter.
                break
    #print(f"After freq check {letter_bank}")
    return letter_bank

#for testing: draw_letters()

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass