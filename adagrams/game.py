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
print("Welcome to Adagrams!")
print("Let's draw 10 letters from the letter pool...")
print("You have drawn the letters:")

def draw_letters():
    return_list = []
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
                return_list.append(random_letter_val)
                counter += 1

    return return_list
    
print(draw_letters())

    # Funtion 1 Comment Walkthrough:
    # While loop to return 10 random letters and their values
    # Choose an integer position random between 1 and 26
    # Add LETTER_POOL[random int] to return_list
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
    # *REMOVES* from letter bank so does not CHANGE letter bank
    # The [:] makes a shallow copy of the array, hence allowing you to modify your copy without damaging the original
    
    # Alternate solution: 
    #draw_letters() = letter_bank
    # word_list = []
    # for char in word.upper():
    #     word_list.append(char)
    
    # i = 0
    # while all(char in letter_bank for char in word_list):
    #     for letter in letter_bank:
    #         for word in word_list:
    #             if word_list.count(char) == letter_bank.count(letter):
    #                 return True
    #             else: 
    #                 return False
    #     i += 1
    # return False

    # all: Return True if all elements of the iterable are true (or if the iterable is empty)
    # .count: returns the number of elements with the specified value.

def score_word(word):
    score = 0
    for letter in word:
        score += LETTER_POOL_VALS.get(letter.upper())
    if len(word) > 6:
        score += 8
    return score

    # Function 3 Comment Walkthrough:
    # Creates dictionary for letters and values
    # Elif for if letter in word - adds points, or not, does nothing
    # If length of word 8+, adds additional 8 points
    # .upper returns strings where all letters are uppercase
    # .get returns the value associated with a specific key

def get_highest_word_score(word_list):
    # Returns tuple - index 0 string of word, index 1 the score of the word
    # If length of word1 == length of word2, tie break: 
    # Shortest length wins, unless length == 10 letters
    pass