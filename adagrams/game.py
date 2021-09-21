import random
def draw_letters():

    letter_bank = {
    "A" : 9,
    "B" : 2,
    "C" : 2,
    "D" : 4,
    "E" : 12,
    "F" : 2,
    "G" : 3,
    "H" : 2,
    "I" : 9,
    "J" : 1,
    "K" : 1,
    "L" : 4,
    "M" : 2,
    "N" : 6,
    "O" : 8,
    "P" : 2,
    "Q" : 1,
    "R" : 6,
    "S" : 4,
    "T" : 6,
    "U" : 4,
    "V" : 2,
    "W" : 2,
    "X" : 1,
    "Y" : 2,
    "Z" : 1,
    }


    # letter_bank = dict.fromkeys(range(11))
    # keys = random.sample(list(letter_bank), 10)
    letters = []
    i = 0
    keys = letter_bank.keys()
    for i in range(10):
        letters.append(random.choice(list(keys)))
    print(letters)

    letter_bank_copy = letter_bank.copy()
    for letter in letter_bank_copy:
        if letter in letters:
            letter_bank_copy[letter] -= 1
    print(letter_bank_copy)

draw_letters()


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass