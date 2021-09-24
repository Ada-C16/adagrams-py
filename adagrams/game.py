import random 

LETTER_POOL = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 
    'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 
    'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1}

SCORE_CHART = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G") : 2,
    ("B", "C", "M", "P") : 3,
    ("F", "H", "V", "W", "Y") : 4,
    ("K") : 5,
    ("J", "X") : 8,
    ("Q", "Z") : 10,
}

# Wave 1
def draw_letters():
    """
    Takes in no parameters,
    returns an array of random 10 strings from LETTER_POOL
    """
    letters = []
    letter_count = LETTER_POOL.copy()  # could also be letter_bank, but not sure yet
    i = 0
    while len(letters) < 10:
        random_letter = random.choice(list(LETTER_POOL))
        if letter_count[random_letter] > 0:
            letter_count[random_letter] -= 1
            letters.append(random_letter)
        if letter_count[random_letter] < 0:
            letters.remove(random_letter)
        i += 1
    return letters

# Wave 2
def uses_available_letters(word, letter_bank):
    """
    Takes in two parameters: word, letter_bank,
    returns True if every letter in word is available,
    otherwise returns False.
    """
    #this method copies the letter bank list
    letter_bank_duplicate = letter_bank[:]

    for letter in word:
        if letter in letter_bank_duplicate:
            letter_bank_duplicate.remove(letter)
        else:
            return False

    return True

# Wave 3        
def score_word(word):
    """
    Takes one parameter word, 
    returns integer score of string word, 
    returns extra points if word is seven letters or more
    """
    total_score = 0
    word_case_check = word.upper()
    
    for key, value in SCORE_CHART.items():
        for letter in word_case_check:
            if letter in key:
                total_score += value
    
    if len(word) >= 7:
        total_score += 8    
    
    return total_score


# Wave 4
def get_score_dict(word_list):
    score_dict = {}
    for word in word_list:
        word_score = score_word(word)
        score_dict[word] = word_score
    return score_dict


def get_highest_word_score(word_list):
    """
    Takes one parameter word_list to find the highest scoring word,
    returns the winning word tuple: (winning_word, top_score)
    """
    score_dictionary = get_score_dict(word_list)
    top_word = max(score_dictionary, key=score_dictionary.get)
    all_scores = get_score_dict(word_list).values()
    top_word_score = max(all_scores)
    
    ties_list = [(top_word, top_word_score)]
    for word, score in score_dictionary.items():
        if top_word_score == score:
            if len(word) < len(top_word):
                ties_list.insert(0,(word, score))
            elif len(word) == len(top_word):
                ties_list.append((word, score))
            elif len(word) == 10:
               ties_list.clear() 
               ties_list.append((word, score))
            
    highest_word_score = ties_list[0]
    return highest_word_score
    
    # tie-breaking rules:
        # prefer word with fewest letters
        # if top_score is btwn multiple words
            # word with len() == 10 is winning_word
        # if multiple words have same total_score, same len()
            # store these in a tie_list
            # winning_word == tie_list[0]