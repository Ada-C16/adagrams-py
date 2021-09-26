import random

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
    hand_of_letters = []
    letter_pool_list = []

    for letter_dict in LETTER_POOL:
        for key in letter_dict:
            freq = letter_dict[key]["frequency"]
            for i in range(0, freq):
                letter_pool_list.append(key)

    for i in range(10):
        index = random.randint(0, len(letter_pool_list)-1)
        letter = letter_pool_list[index]
        hand_of_letters.append(letter)
        letter_pool_list.pop(index)

    return hand_of_letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]
    word_character_list = list(word)

    for letter in word_character_list:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False 
    return True

def score_word(word):
    total_score = 0

    word = word.upper()

    for letter in word:
        for letter_dict in LETTER_POOL:
            for letter_key, letter_data in letter_dict.items():
                if letter_key == letter:
                    total_score += letter_data["point_value"]
            
    if len(word) >= 7:
        total_score += 8

    return total_score

def get_highest_word_score(word_list):
    top_word = ""
    top_score = 0

    for word in word_list:
        if score_word(word) > top_score:
            top_word = word 
            top_score = score_word(word)
        elif score_word(word) == top_score:
            if len(word) == 10 and len(top_word) == 10:
                continue
            elif len(top_word) == 10:
                continue 
            elif len(word) == 10 or len(word) < len(top_word):
                top_word = word
                top_score = score_word(word)

    best_word = [top_word, top_score]
    return best_word