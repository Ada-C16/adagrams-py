def draw_letters():
    pass

def uses_available_letters(word, letter_bank):
    letter_bank_letter_count = {}
    for letter in letter_bank:
        if letter in letter_bank_letter_count:
            letter_bank_letter_count[letter] += 1
        else:
            letter_bank_letter_count[letter] = 1

    for letter in word:
        # if a letter in word is in the letter_bank, 
        # then remove one of the counts from the letter tally in the dict
        # to signify that letter in the letter_bank has been taken
        if letter in letter_bank_letter_count and letter_bank_letter_count[letter] > 0:
            letter_bank_letter_count[letter] -= 1
        else:
            return False

    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass