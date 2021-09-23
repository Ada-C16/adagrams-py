import random

LETTER_POOL = {
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
    'O': 8, 
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

# |Letter                        | Value|
# |:----------------------------:|:----:|
# |A, E, I, O, U, L, N, R, S, T  |   1  |
# |D, G                          |   2  |
# |B, C, M, P                    |   3  |
# |F, H, V, W, Y                 |   4  |
# |K                             |   5  |
# |J, X                          |   8  |
# |Q, Z                          |   10 |

LETTER_POOL_VALS = {
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


def draw_letters():
    hand = []
    letter_freq = {}
    counter = 0
    
    while counter < 10:

            random_letter_index = random.randint(0,25)
            random_letter_val = list(LETTER_POOL.keys())[random_letter_index]
            if random_letter_val in letter_freq:
                letter_freq[random_letter_val] += 1
            else:
                letter_freq[random_letter_val] = 1

            if letter_freq[random_letter_val] <= LETTER_POOL[random_letter_val]:
                hand.append(random_letter_val)
                counter += 1

    return hand

    # Funtion 1 Comment Walkthrough:
    # While loop to return 10 random letters and their values
    # Choose an integer position random between 1 and 26
    # Add LETTER_POOL[random int] to hand
    # Grab just the keys of the dictionary and convert those to a list.
    # Then grab the index of that list using the random_letter number (1-26)
    # Because lists are 0-based, we need to subtract 1 otherwise we grab the letter before
    # Before appending the random letter, we need to look up and make sure it is not appearing more than the value in LETTER_POOL
    # Adds selected letter to list
    # Returns list

def uses_available_letters(word, letters):
    letter_found = True
    letter_bank = letters[:]
    
    while letter_found:
        for letter in word:
            if letter in letter_bank:
                letter_found = True
                letter_bank.remove(letter)
            else:
                letter_found = False

        return letter_found
    
    # Function 2 Comment Walkthrough:
    # Check to see if letters are in available word bank
    # Create a while loop to hold the status of whether we found the letter
    # Elif returns True if in bank, False if not
    # The [:] makes a copy of the array

def score_word(word):
    score = 0
    for letter in word:
        score += LETTER_POOL_VALS.get(letter.upper())
    if len(word) > 6:
        score += 8
    return score

    # Function 3 Comment Walkthrough:
    # Creates dictionary for letters and values
    # If for if letter in word - adds points, or not, does nothing
    # If length of word 8+, adds additional 8 points
    # .upper returns strings where all letters are uppercase
    # .get returns the value associated with a specific key

def get_highest_words_and_score(word_list):
    # Helper Function
    highest_words = []
    highest_score = 0

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score

    for word in word_list:
        score = score_word(word)
        if score == highest_score:
            highest_words.append(word)

    return highest_words, highest_score

def get_highest_word_score(word_list):
    highest_words, highest_score = get_highest_words_and_score(word_list)
    # First element is highest words, second element is highest score in tuple return
    winning_word = highest_words[0]
    
    for word in highest_words:
        if len(word) == 10:
            winning_word = word
            break
        else: 
            if len(word) < len(winning_word):
                winning_word = word

    return winning_word, highest_score


    # Function 4 Comment Walkthrough: 
    # Calls on the helper function to bring in the highest scoring word and the highest score of that word
    # Creates the winning word variable which is the first index in the highest words list
    # Loops through the words in the highest words list - if length of word == 10, winning word is updated to that word, and breaks the loop
    # Else: if length of word is less than the length of the winning word, then winning word becomes that word 
    # Returns the winning word and it's score