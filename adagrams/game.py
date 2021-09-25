import random 
LONG_WORD_MIN = 7
LONG_WORD_MAX = 10
LONG_WORD_POINTS = 8

def build_letter_pool():
    letter_pool = {
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
    return letter_pool

def build_letter_pool_list(letter_pool):
    list_letter_pool = []
    for letter, frequency in letter_pool.items():
        for i in range(frequency):
            list_letter_pool.append(letter)
    return list_letter_pool

def draw_letters():
    letter_pool_dict = build_letter_pool()
    # Convert into a list to ensure weighted probability 
    letter_pool_list  = build_letter_pool_list(letter_pool_dict)
    # random sample function returns list of K size
    player_hand = random.sample(letter_pool_list, k=10) 
    return player_hand

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for char in word:
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False
    return True
    

def build_score_chart():
    score_chart = {
        "A": 1,
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10
    }
    return score_chart


def score_word(word):
    score_chart = build_score_chart()
    score = 0
    cap_word = word.upper()
    
    for char in cap_word:
        if not char:
            return 0
        else:
            point = score_chart[char]
            score += point
    if LONG_WORD_MIN <= len(cap_word) <=LONG_WORD_MAX:
        return score + LONG_WORD_POINTS
    return score 


def get_highest_word_score(word_list):
    points_list = []

    for word in word_list:
        points = score_word(word)
        points_list.append(points)
    
    highest_points = max(points_list)
    # Highest_points_index and highest_word are for no tie cases
    highest_points_index = points_list.index(highest_points)
    highest_word = word_list[highest_points_index]

    # Tie case variable
    index_list = []
    high_word_list = []
    winning_word = ""

    if points_list.count(highest_points) == 1:
        return highest_word,highest_points
    else:
        high_word_list = get_high_word_list(points_list, word_list)
        print(f"{high_word_list=}")
        
        ten_letters = []
        for word in high_word_list:
            if len(word) == 10:
                ten_letters.append(word)
                winning_word = ten_letters[0]
                if len(ten_letters) >= 1:
                    break
            else: 
                short_word_list = find_shortest_length(high_word_list)
                if len(short_word_list) == 1:
                    winning_word = short_word_list[0]
                else:
                    # When we have more than one word
                    winning_word = short_word_list[0]
                    
        return winning_word, highest_points

def get_high_word_list(points_list, word_list):
    index_list = []
    high_word_list = []
    for i in range(len(points_list)):
        if points_list[i] == max(points_list):
            index_list.append(i)
        # Need to use index list to get word
    for index_value in index_list:
        high_word_list.append((word_list[index_value]))
    return high_word_list

def find_shortest_length(high_word_list):
    shortest_word = min(high_word_list, key=len)
    short_list = []

    for word in high_word_list:
        if len(word) == len(shortest_word):
            short_list.append(word)
    return short_list
