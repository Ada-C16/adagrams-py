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
    
    word_score = score
    
    if 7 <= len(word) <= 10:
            word_score +=8

    final_score = word_score    
    
    return final_score


#     return score int(sum)
#     """
# def get_highest_word_score(word_list):
#     pass