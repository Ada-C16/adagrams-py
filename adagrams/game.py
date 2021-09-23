from random import choices

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
# Wave 1

def draw_letters():
    ''' Return a hand of 10 randomly selected letters for user.'''
    letter_bank = {}

    # Randomly select a letter according to its weight in LETTER_POOL
    while sum(letter_bank.values()) < 10:
        letter_pool_keys = list(LETTER_POOL.keys())
        weighted_values = list(LETTER_POOL.values())
        # random.choices(population, weights, k) --> returns single letter list
        letter = choices(letter_pool_keys, weighted_values, k=1)
        letter = letter[0]
    
        if letter in letter_bank:
            # Ensure letter does not occur more frequently than in LETTER_POOL 
            if letter_bank[letter] >= LETTER_POOL[letter]:
                pass
            else:
                # Increment letter frequency
                letter_bank[letter] = letter_bank.get(letter, 0) + 1
        else:
            # Add letter
            letter_bank[letter] = 1

    # Format return list
    letter_bank_list = []
    for letter, freq in letter_bank.items():
        letter_bank_list.append(letter * freq)

    letter_bank_str = "".join(letter_bank_list)

    # Alternate way to format return list 
    # letter_bank_list = "".join([v * k for k, v in letter_bank.items()])

    return list(letter_bank_str)
    
# Wave 2

def uses_available_letters(word, letter_bank):
    ''' Check that user's input word only contains letters that occur
    in user's collection of drawn letters.'''
    # Copy letter_bank to preserve original data
    letter_bank_2 = letter_bank[:]

    # Check for presence of each letter in drawn letters
    for letter in word:
        if letter not in letter_bank_2:
            return False
        else:
            letter_bank_2.remove(letter)
    return True

# Wave 3

def score_word(word):
    ''' Return score of word according to rules of Adagrams game.'''
    score = 0

    # Adagrams scoring data
    scores = [
            ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S'], # 1 points
            ['D', 'G'], # 2 
            ['B', 'C', 'M', 'P'], # 3 
            ['F', 'H', 'V', 'W', 'Y'], #4 
            ['K'], #5 
            ['J', 'X'], #8 
            ['Q', 'Z'], #10 
    ]

    # Locate letter, hardcode points
    for letter in word:
        letter = letter.upper()
        if letter in scores[0]: #['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S']
            score += 1
        elif letter in scores[1]: #['D', 'G']
            score += 2
        elif letter in scores[2]: #['B', 'C', 'M', 'P']
            score += 3
        elif letter in scores[3]: #['F', 'H', 'V', 'W', 'Y']
            score += 4
        elif letter in scores[4]: #['K']
            score += 5
        elif letter in scores[5]: #['J', 'X']
            score += 8
        elif letter in scores[6]: #['Q', 'Z']
            score += 10

    # Adagrams awards +8 points for words between 7-10 chars
    if 7 <= len(word) <= 10:
        score += 8

    return score

# Wave 4

def get_highest_word_score(word_list):
    ''' Calculate word with highest score, applying Adagrams tie-breaking 
    logic, and return the winning word in a special data structure.'''
    # Score each word, store in words_scores_dict
    words_scores_dict = {}
    for word in word_list:
        words_scores_dict[word] = score_word(word)
    
    # Find highest scores, scores stored in words_scores_dict[values]
    highest_score = max(words_scores_dict.values())
    words_with_highest_scores = [k for k, v in words_scores_dict.items() \
                                   if v == highest_score]

    # Alternate way to obtain words_with_highest_scores
    # words_with_highest_scores = []
    # for word, score in words_scores_dict.items():
    #    if score == highest_score:
    #        word_with_highest_scores.append(word)

    # words_with_highest_scores output: ['BBBBBB', 'AAAAAAAAAA']

    # Max, min functions return first respective value
    longest_word = max(words_with_highest_scores, key=len)
    shortest_word = min(words_with_highest_scores, key=len)

    # A word of length 10 wins outright
    if len(longest_word) == 10:
        return (longest_word, score_word(longest_word))
    # Otherwise the shortest word wins
    else:
        return (shortest_word, score_word(shortest_word))