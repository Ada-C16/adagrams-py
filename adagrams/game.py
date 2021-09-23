import random

def display_welcome_message():
    print("Welcome to Adagrams!")


def display_drawn_letters(letters):
    print("You have drawn the letters:")
    print(', '.join(letters))


def draw_letters():
    display_welcome_message()

    # Original letter pool that remains constant. 
    LETTER_POOL = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 
        'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 
        'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 
        'Z': 1
    }

    # Reconstructing LETTER_POOL into a list that contains all of the 
    # possible letter choices.
    
    letter_choices = []
    expanded_letter_pool = []

    for alphabet, distribution in LETTER_POOL.items():
        letter_choices.append(alphabet * distribution)

    letter_string = "".join(letter_choices)

    expanded_letter_pool = list(letter_string)

    # Selecting 10 letters from expanded_letter_pool to create letter_bank.
    letter_bank = random.sample(expanded_letter_pool, 10)
    display_drawn_letters(letter_bank)
    return letter_bank


def display_game_instructions():
    print("Please input your submission for the longest anagram you can come up with")


def display_needs_valid_input_message():
    print("You entered in a word that contains characters not in the letter bank")


def uses_available_letters(word, letter_bank):
    display_game_instructions()
#Call function to display game instructions and prompt user to enter a word
#Make a copy of the letter bank to use during round
#So it doesn't change the letter_bank list directly
    user_letters = letter_bank.copy()
#try statement to raise error if not enough letters
#look at letters in word and remove letters
#will return true if all letters are in word
#if runs out of letter
#remove() method raises an ValueError exception, if specified item doesn’t exist in a list.    
    try: 
        for letter in word:
            user_letters.remove(letter)
        return True

    except ValueError:
        display_needs_valid_input_message()
        return False 


def display_score(score):
    print(f"Your submitted anagram scored {score} points")


def score_word(word):
#to avoid case conflicts, assign word to a new variable and add .upper so it's able to compare
#start the scoreboard with zero    
#list of tuples for the board and score points    
    user_word = word.upper()
    score = 0
    point1 = ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T")
    points2 = ("D", "G")
    points3 = ("B", "C", "M", "P")
    points4 = ("F", "H", "V", "W", "Y")
    points5 = ("K")
    points8 = ("J", "X")
    points10 = ("Q", "Z")

#iterate through each letter in the word that was submitted to score
#if the letter is found in the list of tuples, assign appropriate value
#move down the list for all the letters
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
#Totals up the score for the word only
#Bonus points for a word that is between 7-10 letters long of 8 points
#add up word score plus total bonus, to return the final score
    if 7 <= len(word) <= 10:
            word_score +=8
    final_score = word_score  
    display_score(score)
    return final_score  


def display_retry_instructions():
    print("Should we play another round?")
    print("Enter y to replay")


def display_highest_score(word_score):
    print("Thanks for playing Adagrams!")
    print(f"The highest score from this game was {word_score[0]}, which was worth {word_score[1]} points.")


def get_highest_word_score(word_list):
    word_scores = []
    for word in word_list:
        word_scores.append((word, score_word(word)))

    high_score_words = []
    max_score = 0
    for i, (word, score) in enumerate(word_scores):
        if max_score == score:
            high_score_words.append(word_scores[i])
        elif max_score < score:
            high_score_words = [word_scores[i]]
            max_score = score

    if len(high_score_words) == 1:
        return high_score_words[0]
    tied_words = []

    for (word, score) in high_score_words:
        tied_words.append(word)

    shortest_word_length = len(sorted(tied_words, key=len)[0])

    # Tiebreaker: if words the same length, return first value as loop iterates
    # Tiebreaker: word length equals 10 wins
    # Tiebreaker: shortest word wins
    for i, (word, score) in enumerate(high_score_words):
        if len(word) == 10:
            return high_score_words[i]
        elif len(word) == shortest_word_length:
            tiebreaker = high_score_words[i]

    display_highest_score(tiebreaker)

    return tiebreaker


display_retry_instructions()


def display_goodbye_message():
    print("Goodbye!")


display_goodbye_message()
