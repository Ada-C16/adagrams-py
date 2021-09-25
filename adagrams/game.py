import random
LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
    'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4,
    'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}


def draw_letters():
    """
    Build a hand of 10 letters for the user. Returns an array of strings
    with one letter in each string. The num of strings included in the array 
    cannot be more than the num alloted to that letter in the letter table
    """
    letter_to_draw = list(LETTER_POOL.keys())
    letters_drawn = []
    letter_count = {}
    for letter in random.sample(letter_to_draw, 10):
        if letter not in letters_drawn:
            letter_count[letter] = 0
            letters_drawn.append(letter)
            letter_count[letter] = 1
        elif letter_count[letter] < LETTER_POOL[letter]:
            letters_drawn.append(letter)
            letter_count[letter] += 1

    return letters_drawn


def uses_available_letters(word, letter_bank):
    """
    This function will compare the letters in the user's word to the letter_bank.
    If letters in user's word are not in letter_bank, or if the user uses more letters
    than they have, the function will return False. 
    Function will return False if the user doesn't empty a word. Else, it returns True.
    """
    for letter in word:
        if letter not in letter_bank:
            is_valid = False
        if word.count(letter) > letter_bank.count(letter):
            is_valid = False
        else:
            is_valid = True

    return is_valid


LETTER_POINTS = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}  # changed to caps to signifiy sentinel variable; may want this at top of file.


def score_word(word):
    """
    This function will calculate the user's score for their entered word.
    It needs to calculate a score that ignores the lettercase, takes into
    account an empty word, and gives extra points for longer words.
    """
    total = 0
    # created variable to demonstrate significance of these nums
    bonus_range = [7, 8, 9, 10]
    for letter in word.upper():
        total += LETTER_POINTS[letter]
    if len(word) in bonus_range:
        total += 8

    return total


def get_highest_word_score(word_list):
<<<<<<< HEAD
    words_scored_dict = {}
    for user_word in word_list:
        words_scored_dict[user_word] = score_word(user_word)
    winning_list = []
    winning_combo = None
    for user_word, score in words_scored_dict.items():
        if len(user_word) == 10:
            return user_word, score
        else:
            if score == max(words_scored_dict.values()):
                if len(user_word) < 10:
                    winning_list.append((user_word, score))
    max_word_len = 0
    for word_combo in winning_list:
        if len(word_combo[0]) > max_word_len:
            max_word_len = len(word_combo[0])
        if len(word_combo[0]) < max_word_len:
            winning_combo = word_combo
            return winning_combo
        else:
            winning_combo = winning_list[0]
    return winning_combo
=======
    """
    - create a function that gets the highest score in the game
    - return a tuple that has the first item as the word with its score
    - tuple first element string of word, second element = score of word
    - if tie for highest score, winner is the word with the fewest number of letters
    - UNLESS a word has exactly 10 letters
    - if words same score same length or both 10 letters, just pick first word in list
    """
    words_scored_dict = {}
    for user_word in word_list:
        words_scored_dict[user_word] = score_word(user_word)
    
    # max_score_word = (user_word,max(words_scored_dict[user_word]))
    # # print(max_score_word)
    # ten_letter_words = []
    # max_score = 0
    # max_score_list = []
    # for user_word,score in words_scored_dict.items():
    #     if len(user_word) == 10:
    #         ten_letter_words.append(user_word,score)
    #         return ten_letter_words[0]
    #     else:
    #         if max_score < score:
    #             max_score = score
    #         elif max_score == score:
    #             max_score_list.append(user_word, score)
    #         winning_word = min(len(max_score_list[user_word][0]))
    #         return winning_word
   

    


>>>>>>> 7f1428dc9e9bcb483570786e6a65f7349ca4894f
