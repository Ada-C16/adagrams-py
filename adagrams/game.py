import random

def draw_letters():
    pass

def uses_available_letters(word, letter_bank):
    matched_list=[characters in letter_bank for characters in word]
    string_contains_chars = all(matched_list)
    return string_contains_chars


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass