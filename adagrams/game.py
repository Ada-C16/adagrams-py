import random


def draw_letters():
    letters_dict = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3,
                    'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1,
                    'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, "Z": 1}

    # for every key in the dictionary, we are multiplying it by its value and adding it to our list
    # when we multiply, we made i a list because we can't multiply strings by integers (for example, we can't multiply 'A' * 9)
    # however we can multiply list of strings by integers (for example, ['a']*9 = ['a','a','a','a', etc])
    # extend is used to then combine that list with the one we created
    letter_list = []
    for i in letters_dict:
        multiplied = list(i) * letters_dict[i]
        letter_list.extend(multiplied)

    # random.sample is pulling 10 random letters from our list and removing them so we don't pull two Zs or Xs
    # works like pop function but returns random
    ten_letters = random.sample(letter_list, k=10)
    return ten_letters


def uses_available_letters(word, letter_bank):
    # create a copy of the list passed into letter_bank to avoid unwanted side-effects and changing the original list.
    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy.append(letter)

    # iterate through the string argument passed into the word parameter, and add each letter in the word to a list.
    letters_in_word = []
    for letter in word:
        letters_in_word.append(letter)

    # Create a new list for storing the letters that we will use from the letter bank.
    # Iterate through each letter in letters_in_word list.
        # If a letter from that list is also in the letter bank, we will:
        # 1) Add it to the list of used letter bank letters
        # 2) Remove it from our copy of the letter_bank list
    letter_bank_used = []
    for letter in letters_in_word:
        if letter in letter_bank_copy:
            letter_bank_used.append(letter)
            letter_bank_copy.remove(letter)

    # If the length of the argument passed into word is equal to the length of the letter_bank_used list, return True.
    # Otherwise, return false.
    if len(word) == len(letter_bank_used):
        return True
    else:
        return False


def score_word(word):
    # Create a dictionary for the scores of each letter, where the letter is the key, and its score is the corresponding value
    score_dict = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2,
                "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1,
                "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4,
                "X": 8, "Y": 4, "Z": 10
            }

    # Format the input so that each letter in the string argument passed into word parameter is uppercase (to pass the test that ignores case)
    # Store into new variable to be used in score calculation
    word_formatted = word.upper()

    # Create a new list, and iterate over word, storing each letter into the new list.
    letters_in_word = []
    for letter in word_formatted:
        letters_in_word.append(letter)

    # Create a counter variable to tally the score. Iterate over each letter in the letters_in_word list.
        # Referencing the score_dict dictionary, use each letter as a key to add its corresponding value to the score counter.
    score = 0
    for letter in letters_in_word:
        score += score_dict[letter]

    # If the length of the word is 7, 8, 9, or 10, add 8 points to the score
    if len(word) >= 7:
        score += 8

    return score


def get_highest_word_score(word_list):
    # get the score of each word by iterating through the word_list and using the score_word function
    # create a new dictionary to store the words as a keys and the scores as its value
    words_and_scores = {}
    for word in word_list:
        score = score_word(word)
        words_and_scores[word] = score

    # all_scores is our variable that stores a list of all the scores and max_score finds the highest score
    # we then find the words that have the highest score by iterating through our dictionary
    # create a new list to put all the words that the highest score as their value
    all_scores = words_and_scores.values()
    max_score = max(all_scores)
    words_with_max = []
    for word in words_and_scores:
        if words_and_scores[word] == max_score:
            words_with_max.append(word)

    # if there's only one word in our list: add the score and return the list as a tuple
    if len(words_with_max) == 1:
        words_with_max.append(max_score)
        return tuple(words_with_max)
    # if multiple words and one word's length is 10: return the word with 10 letters and its score as tuple
    for word in words_with_max:
        if len(word) == 10:
            return tuple([word, max_score])
    # if multiple words and not a length of 10: return the word with fewest letters and its score as a tuple
    # iterate through our list of words with the max score to find the word with the shortest length
    lengths = [len(i) for i in words_with_max]
    shortest_length = min(lengths)
    for word in words_with_max:
        if len(word) == shortest_length:
            return tuple([word, max_score])
    # these will all automatically return the first one if lengths are the same
