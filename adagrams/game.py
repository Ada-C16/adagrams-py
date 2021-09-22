def draw_letters():
    '''
    build a hand of 10 letters for the user

    - Returns an array of ten strings (one letter each)
    - These represent the hand of letters that the player has drawn
    - The letters should be randomly drawn from a pool of letters
    '''
    import random 
    # drawling pool
    available_tiles = {
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
        'O': 18, 
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
    pool = []
    
    for letter, count in available_tiles.items():
        pool += letter *count
    
    # randomly select from pool
    return random.sample(pool, 10)


import copy
def uses_available_letters(word, letter_bank):
    #https://docs.python.org/2/library/copy.html#copy.deepcopy

    letter_bank_carbon_copy = copy.deepcopy(letter_bank)
    for letter in word:
        if letter in letter_bank_carbon_copy:
            letter_bank_carbon_copy.remove(letter)

        else:
            return False
        
    return True
    

def score_word(word):
    '''
    `score_word` in `game.py` has the following properties:

    - Has one parameter: `word`, which is a string of characters
    - Returns an integer representing the number of points
    - Each letter within `word` has a point value. 
        The number of points of each letter is summed up to represent
        the total score of `word`
    - Each letter's point value is described in the table below
    - If the length of the word is 7, 8, 9, or 10, then the word 
        gets an additional 8 points
    '''
    score_chart = {
        'A': 1, 
        'B': 3, 
        'C': 3, 
        'D': 2, 
        'E': 1, 
        'F': 4, 
        'G': 2, 
        'H': 4, 
        'I': 1, 
        'J': 8, 
        'K': 5, 
        'L': 1, 
        'M': 3, 
        'N': 1, 
        'O': 1, 
        'P': 3, 
        'Q': 10, 
        'R': 1, 
        'S': 1, 
        'T': 1, 
        'U': 1, 
        'V': 4, 
        'W': 4, 
        'X': 8, 
        'Y': 4, 
        'Z': 10
        }
    score = 0
    # add score for each letter
    # convert to uppercase
    for letter in word:
        score += score_chart[letter.upper()]
    # bonus points for word length
    if 7 <= len(word) <= 10:
        score += 8
    return score 


def get_highest_word_score(word_list):
    ''' 
    `get_highest_score` in `game.py` has the following properties:

    - Has one parameter: `word_list`, which is a list of strings
    - Returns a tuple that represents the data of a winning word and it's score.  
      The tuple must contain the following elements:
        - index 0 ([0]): a string of a word
        - index 1 ([1]): the score of that word
    - In the case of tie in scores, use these tie-breaking rules:
        - prefer the word with the fewest letters...
        - ...unless one word has 10 letters. If the top score is tied between 
        multiple words and one is 10 letters long, choose the one with 10 
        letters over the one with fewer tiles
        - If the there are multiple words that are the same score and the 
        same length, pick the first one in the supplied list
    '''
    # build score board for all words submitted
    score_board = {word:score_word(word) for word in word_list}
    
    # get a highest scoring word
    winning_words = [word for word,score in score_board.items() if score == max(score_board.values())]
    
    if len(winning_words) > 1: # tie logic
        # make new scoreboard using word and its length
        tie_chart = {word:len(word) for word in winning_words}
        # highest and lowest score
        first_max = max(tie_chart, key = tie_chart.get)
        
        # if there is a 10
        if tie_chart[first_max] == 10:
            winning_word = [k for k,v in tie_chart.items() if v == 10][0]
        else: # no tens, default to lowest score
            first_min = min(tie_chart, key = tie_chart.get)
            winning_word = [k for k,v in tie_chart.items() if v == tie_chart[first_min]][0]
        winner = [winning_word, score_board[winning_word]]
    
    else: # only one winner
        winner = [winning_words[0], score_board[winning_words[0]]]
    return winner

    
