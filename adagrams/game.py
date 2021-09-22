# import ui_helper

def draw_letters():
    import random

    # Original letter pool that remains constant. 
    LETTER_POOL = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 
        'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 
        'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 
        'Z': 1
    }

    # reconstructing LETTER_POOL into a list that contains all of the 
    # possible letter choices.
    
    letter_choices = []
    expanded_letter_pool = []

    for alphabet, distribution in LETTER_POOL.items():
        letter_choices.append(alphabet * distribution)

    letter_string = "".join(letter_choices)

    for letter in letter_string:
        expanded_letter_pool.append(letter)
    
    # Selecting 10 letter from expanded_letter_pool to create letter_bank.
    letter_bank = random.sample(expanded_letter_pool, 10)
    
    return letter_bank


def display_needs_valid_input_message():
    print("You entered in a word that contains characters not in the letter bank")
    # ui_helper.display_game_instructions()

def uses_available_letters(word, letter_bank):
#Call function to display game instructions and prompt user to enter a word
    # ui_helper.display_game_instructions()
#Make a copy of the letter bank to use during round
#So it doesn't change the letter_bank list directly
    user_letters = letter_bank.copy()
#try statement to raise error if not enough letters
#look at letters in word and remove letters
#will return true if all letters are in word
    try: 
        for letter in word:
            user_letters.remove(letter)
        return True
#if runs out of letter
#remove() method raises an ValueError exception, if specified item doesn’t exist in a list.
    except ValueError:
        display_needs_valid_input_message()
        return False 


def score_word(word):
    user_word = word.upper()

    score = 0
    
    point1 = ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T")
    points2 = ("D", "G")
    points3 = ("B", "C", "M", "P")
    points4 = ("F", "H", "V", "W", "Y")
    points5 = ("K")
    points8 = ("J", "X")
    points10 = ("Q", "Z")
    
    for letter in user_word:
        if letter in point1:
            score += 1
        elif letter in points2:
            score += 2
        elif letter in points3:
            score += 3
        elif letter in points4:
            score += 4
        elif letter in points5:
            score += 5
        elif letter in points8:
            score += 8
        elif letter in points10:
            score += 10
    
    word_score = score  # does score need to be reassigned?
    
    if 7 <= len(word) <= 10:
            word_score +=8

    final_score = word_score  # same as above.
    
    return final_score  # can return score


def get_highest_word_score(word_list):
    word_scores = []
    for word in word_list:
        word_scores.append((word, score_word(word)))

    max_score = 0
    for i, (word, score) in enumerate(word_scores):
        if max_score == score:
            high_score_words.append(word_scores[i])
        elif max_score < score:
            high_score_words = [word_scores[i]]
            max_score = score
    if len(high_score_words) == 1:
        return high_score_words[0]

    # Sorting tied words to find the shortest string length 
    # to compare for tiebreakers.
    tied_words = []
    for (word, score) in high_score_words:
        tied_words.append(word)
    sortedwords = sorted(tied_words, key=len)
    print(sortedwords)

    # Tiebreaker: if words the same length, return first value
    # Tiebreaker: shortest word wins
    # Tiebreaker: word length equals 10 wins
    for i, (word, score) in enumerate(high_score_words):
        if len(word) == 10:
            return high_score_words[i]
        elif len(word) == len(sortedwords[0]):
            tiebreaker =high_score_words[i]

    return tiebreaker
