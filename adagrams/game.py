import random
# module will let us randomly choose characters in specified sample range

def draw_letters():
    """
    Build a hand of 10 letters for the user. Returns an array of strings, one letter long.
    The num of strings included in the array 
    cannot be more than the num alloted in the letter table
    """
    LETTER_POOL = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4,
        'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }
    letter_to_draw = list(LETTER_POOL.keys())
    letters_drawn = []
    letter_count = {}
    for letter in random.sample(letter_to_draw, 10):
        if letter not in letters_drawn:
            letters_drawn.append(letter)
            letter_count[letter] = 1
        elif letter_count[letter] < LETTER_POOL[letter]:
            letters_drawn.append(letter)
            letter_count[letter] += 1

    return letters_drawn


def uses_available_letters(word, letter_bank):
    """
    If letters in user's word are not in letter_bank, or if user uses more letters
    than in hand, the function returns False. 
    Function returns False if user enters empty word. Else, it returns True.
    """
    for letter in word:
        if letter not in letter_bank or word.count(letter) > letter_bank.count(letter):
            is_valid = False
        else:
            is_valid = True

    return is_valid


def score_word(word):
    """
    Calculate  user's score for their entered word.
    Ignore lettercase, account for empty word, and give extra points for longer words.
    """
    LETTER_POINTS = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
        'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
        'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }
    bonus_range = [7, 8, 9, 10]
    total = sum([LETTER_POINTS[letter] for letter in word.upper()])
    if len(word) in bonus_range:
        total += 8

    return total


def get_highest_word_score(word_list):
    """
    Score the words in word_list. Returns tuple of word with highest score.
    If tie score, word with 10 letters or word with least letters wins.
    """
    words_scored_dict = {user_word: score_word(
        user_word) for user_word in word_list}

    highest_word_score = max(words_scored_dict.values())
    smallest_word_len = min((len(key) for key in words_scored_dict.keys()))
    largest_word_len = max((len(key) for key in words_scored_dict.keys()))

    for user_word, score in words_scored_dict.items():
        if largest_word_len == 10:
            if len(user_word) != 10:
                continue
            elif len(user_word) == 10:
                winning_word = user_word
                highest_word_score = score
                break
        elif score == highest_word_score and len(
                user_word) == smallest_word_len:
            winning_word = user_word
            break
        elif score == highest_word_score:
            winning_word = user_word

    return winning_word, highest_word_score
