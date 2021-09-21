# from tests.test_wave_01 import LETTER_POOL


# def draw_letters():

def display_game_instructions():
    print("Please input your submission for the longest anagram you can come up with")

def display_needs_valid_input_message():
    print("You entered in a word that contains characters not in the letter bank")
    display_game_instructions()

def uses_available_letters(word, letter_bank):
#Call function to display game instructions and prompt user to enter a word
    display_game_instructions()
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

# def score_word(word):
#     """
#     score = 0
#     dictionary mapping - to refer table 
#     add up value (sum)
#     score += value
#     return score int(sum)
#     """
# def get_highest_word_score(word_list):
#     pass