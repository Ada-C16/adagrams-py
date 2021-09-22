
# import random module
import random

# create a constant variable called LETTER_POOL which will be a tuple
# filled with nested dictionaries that hold the letter info
# 
# example: 
LETTER_POOL = (
    {"A" : {
        "frequency" : 9,
        "point_value" : 1
        }
    },
    { "B" : {
        "frequency" : 2,
        "point_value" : 3
        }
    }
)


def draw_letters():
    hand_of_letters = []
    # create an empty list that will eventually hold
    # 10 strings,  letter "hand of letters"
    letter_pool_list = []
    # create an empty list that will eventually hold all 
    # the letters in letter pool in accurate frequency. 
    # example of how list will eventually look like: 
    # letter_pool_list = ["A","A","A","A","A","A","A","A","A","B","B" etc...]
    for letter in LETTER_POOL:
        letter.keys()
        

    # iterate through the LETTER_POOL tuple with a forloop
    # append each key (which will be a string like "A" or "B") to the list
    # letter_pool_list the appropriate number of times aka the value (which will be 
    # an int like 9 or 2). 
    
    # create a for loop that will run 10x
    #   generate a random int 
    #   select a string from letter_pool_list with the index random int
    #   example: letter_pool_list[random_int]
    #   use the pop(index) function to remove the string at index random_int.

    #   append the popped value to hand of letter list

    # return a list that contains 10 strings ["A", "B", "C" etc...]

def uses_available_letters(word, letter_bank):
    pass

    # returns a boolean value. 
    # True if the word can be spelled with the 10 letters 
    # in the list "letter_bank" that we are passed.
    # False if the word cannote be spelled.

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass


# list = ["a","b","c"]
# hand_draw_letters = []

# picked_letter = list.pop(1)

# #print(picked_letter)
# hand_draw_letters.append(picked_letter)

# print(list)
# print(hand_draw_letters)

draw_letters()