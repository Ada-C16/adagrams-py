
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
    },
    {"C" : {
        "frequency" : 2,
        "point_value" : 3
           }
    },
    {"D" : {
        "frequency" : 4,
        "point_value" : 2
        }
    },
    {"E" : {
        "frequency" : 12,
        "point_value" : 1
        }
    },
    {"F" : {
        "frequency" : 2, 
        "point_value" : 4
        }
    },
    {"G" : {
        "frequency" : 3,
        "point_value" : 2
        }
    },
    {"H" : {
        "frequency" : 2,
        "point_value" : 4
        }
    },
    {"I" : {
        "frequency" : 9,
        "point_value" : 1
        }
    },
    {"J" : {
        "frequency" : 1,
        "point_value" : 8
        }   
    },
    {"K" : {
        "frequency" : 1,
        "point_value" : 5
        }
    },
    {"L" : {
        "frequency" : 4,
        "point_value" : 1
        }
    },
    {"M" : {
        "frequency" : 2,
        "point_value" : 3
        }
    },
    {"N": {
        "frequency" : 6,
        "point_value" : 1
        }
    },
    {"O" : {
        "frequency" : 8,
        "point_value" : 1
        }
    },
    {"P" : {
        "frequency" : 2,
        "point_value" : 3
        }
    },
    {"Q" : {
        "frequency" : 1,
        "point_value" : 10
        }
    },
    {"R" : {
        "frequency" : 6,
        "point_value" : 1
        }
    },
    {"S" : {
        "frequency" : 4,
        "point_value" : 1
        }
    },
    {"T" : {
        "frequency" : 6,
        "point_value" : 1
        }
    },
    {"U" : {
        "frequency" : 4,
        "point_value" : 1
        }
    },
    {"V" : {
        "frequency" : 2,
        "point_value" : 4
        }
    },
    {"W" : {
        "frequency" : 2,
        "point_value" : 4
        }
    },
    {"X" : {
        "frequency" : 1,
        "point_value" : 8
        }
    },
    {"Y" : {
        "frequency" : 2,
        "point_value" : 4
        }
    },
    {"Z": {
        "frequency" : 1,
        "point_value" : 10
        }
    }
)

def draw_letters():
    # create an empty list that will eventually hold
    # 10 strings,  letter "hand of letters"
    hand_of_letters = []

    # create an empty list that will eventually hold all 
    # the letters in letter pool in accurate frequency. 
    # example of how list will eventually look like: 
    # letter_pool_list = ["A","A","A","A","A","A","A","A","A","B","B" etc...]
    letter_pool_list = []

    # iterate through the LETTER_POOL tuple with a forloop
    # append each key (which will be a string like "A" or "B") to the list
    # letter_pool_list the appropriate number of times aka the value (which will be 
    # an int like 9 or 2). 
    for letter_dict in LETTER_POOL:
        for key in letter_dict:
            freq = letter_dict[key]["frequency"]
            for i in range(0, freq):
                letter_pool_list.append(key)
    
    # create a for loop that will run 10x
    # generate a random int 
    # select a string from letter_pool_list with the index position random int
    # example: letter_pool_list[random_int]
    # use the pop(index) function to remove the string at index random_int.
    # append the popped value to hand of letter list
    for i in range(10):
        index = random.randint(0, len(letter_pool_list)-1)
        letter = letter_pool_list[index]
        hand_of_letters.append(letter)
        letter_pool_list.pop(index)

    # return a list that contains 10 strings ["A", "B", "C" etc...
    return hand_of_letters

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

print(draw_letters())