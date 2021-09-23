def score_word(word):
    """
    Returns score of user word per values in letters_value_dict
    """
    # Initialize dictionary with letter values
    letters_value_dict = {
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
    # Initialize sum variable
    sum = 0
    # Change user input to uppercase
    word = word.upper()
    # Loop through each letter in word and find value to add to sum
    for letter in word:
        sum += letters_value_dict.get(letter)
    # Add 8 to sum if word is longer than 6
    if len(word) > 6:
        sum += 8
    # return sum
    return sum


def tie_breaker(same_score_dict, word_list):
    # Issue 1: We were missing the list(). Without this, the return value is "dict_keys(['MMMM', 'WWW'])" instead of "['MMMM', 'WWW']"
    same_score_words = list(same_score_dict.keys())
    # print statement below for reference
    # print(same_score_dict.keys())

    ten_length_words = []
    min_length_words = []
    # Issue 2: We were missing the len(). Without this, the return value is the min length word, not the min length
    min_length = len(min(same_score_words, key=len))
    # print statement below for reference
    # print(min(same_score_words, key=len))
    
    for word in same_score_words: 
        if len(word) == 10:
            ten_length_words.append(word)
        elif len(word) == min_length: 
            min_length_words.append(word)
    
    if len(ten_length_words) == 1: 
        return ten_length_words[0],same_score_dict[ten_length_words[0]]
    elif len(ten_length_words) > 1:
        for word in word_list: 
            if word in ten_length_words:
                return word, same_score_dict[word]
    elif len(min_length_words) == 1: 
        return min_length_words[0], same_score_dict[min_length_words[0]]
    elif len(min_length_words) > 1:
        for word in word_list: 
            if word in min_length_words:
                return word, same_score_dict[word]
    
    
def get_highest_word_score(word_list):
    # initialize variables
    scored_dict = {}
    same_score_dict = {}

    # score each word in word_list and put into dictionary(?)
    for word in word_list: 
        score = score_word(word)
        scored_dict[word] = score

    # identify max value(s)
    all_values = list(scored_dict.values())
    max_value = max(all_values)
    for word, value in scored_dict.items(): 
        if value == max_value:
            same_score_dict[word] = value

    if len(same_score_dict) == 1: 
        print(same_score_dict)
        for key, value in same_score_dict.items():
            return key, value
        # return same_score_dict.keys(), same_score_dict.values()
    else:
        return tie_breaker(same_score_dict, word_list)


def test_get_highest_word_tie_prefers_shorter_word():
    # Arrange
    words = ["MMMM", "WWW"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert score_word(words[0]) == 12
    assert score_word(words[1]) == 12
    assert best_word[0] == "WWW"
    assert best_word[1] == 12

def test_get_highest_word_tie_prefers_shorter_word_unsorted_list():
    # Arrange
    words = ["WWW", "MMMM"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert score_word(words[0]) == 12
    assert score_word(words[1]) == 12
    assert best_word[0] == "WWW"
    assert best_word[1] == 12

test_get_highest_word_tie_prefers_shorter_word()
test_get_highest_word_tie_prefers_shorter_word_unsorted_list()