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
    is_valid = True
    if word == False:
        is_valid = False
    else:
        for letter in word:
            if letter not in letter_bank:
                is_valid = False
            if word.count(letter) > letter_bank.count(letter):
                is_valid = False

    return is_valid


LETTER_POINTS = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
} # changed to caps to signifiy sentinel variable; may want this at top of file.


def score_word(word):
    """
    This function will calculate the user's score for their entered word.
    It needs to calculate a score that ignores the lettercase, takes into
    account an empty word, and gives extra points for longer words. 
    -  assign each letter in the word we pass into the function a point value
    for each_letter in word
    - add the value of each letter together, returning a sum of the total point value of the word 
    - return sum
    - count length of word, If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
    - maybe add 8 points to sum?
    """
    # a dict may be better to easily access the score.
    # could use ints as keys for the score and letters as the value
    # assign each letter in the word we pass in a point value
    total = 0
    bonus_range = [7, 8, 9, 10] # created variable to demonstrate significance of these nums
    for letter in word.upper():
        total += LETTER_POINTS[letter]
    if len(word) in bonus_range:
        total += 8

    return total


def get_highest_word_score(word_list):
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
   

    


