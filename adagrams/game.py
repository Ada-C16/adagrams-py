
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
    #make a copy of the list letter_bank for safe to operate on and change
    letter_bank_copy = letter_bank[:]

    # make a list of characters in the word variable (which is a string)
    word_character_list = list(word)

    # create a loop
    count = 0
    for letter in word_character_list:
        if letter in letter_bank_copy:
            print(letter)
            letter_bank_copy.pop()
            count += 1
        else:
            print(f"The letter {letter} is unavailale")
        letter_bank_copy.pop()
    # create an if statement that compares the letters in the letter bank with the letters
    # in the word 

    # use the pop function to remove a letter from the letter bank copy once it's been 
    # compared with a letter in the word


    # returns a boolean value. 
    # True if the word can be spelled with the 10 letters 
    # in the list "letter_bank" that we are passed.
    # False if the word cannote be spelled.

def score_word(word):
    pass
    # create a variable for the total_score, set the score to 0
    
    # make the string variable we are passed ALL CAPS with the upper() function
    # that way each character in our word will match the dictionary keys in LETTER_POOL
    # example: word = word.upper()

    # make a 3 nested for loops (indentation indicates scope)
    # iterate through each character in the word variable
    #   iterate through each element (we used "letter_dict" in the first function) in LETTER_POOL
    #       iterate through each key in the "letter_dict" to access it's value, which is another dictionary with data about the letter frequency and point value.
    #       i got this expression from the iterating over dictionaries lesson in Learn: "for letter, letter_data in letter_dict.items():"
    #       i'm not sure how to word what it's doing.
    #           compare the key of the dictionary (which will be a letter) to the character in the word from the first loop. if they match add the letter's point 
    #           value to the variable total_score  
    
    # evaluate the length of the word variable
    # make an if statement where if the word is longer than 7 characters add 8 points to total_score

    # return total_score variable

def get_highest_word_score(word_list):

    pass
    # create an empty list variable (best_word) that will eventually hold the best word's data
    # where the first value is the string of the word and the second value is the point value
    # example: best_word = ["reallygoodword", 14]

    #create an empty string variable that will eventually hold the word with the most points (top_word)

    #create a variable for the top score and set it to zero (top_score)

    # iterate through each word in word_list and calculate it's score with the score_word function
    #   compare the score to the variable top_score with if statements.
    #       if the score is bigger than top_score, make that word the top_word and that score top_score
    #       if the score is a tie compare the length of each word with if statements
    #           if one word has exactly 10 letters in it, thats the top_word
    #           if both words have 10 letters the word with the lowest index in word_list is top_word
    #           if neither of the words have 10 letters the shorter word it top_word


    #return the best_word list with top_word as the first value and top_score as the 2nd value
    # best_word = [top_word, top_score]

letter_bank_test = draw_letters()
print(letter_bank_test)
water_character_list = list("WATER")

["W", "A", "T", "E", "R"]

uses_available_letters("WATER", letter_bank_test)

print(letter_bank_test)