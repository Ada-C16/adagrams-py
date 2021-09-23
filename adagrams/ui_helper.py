def display_welcome_message():
    print("Welcome to Adagrams!")

def display_drawn_letters(letters):
    print("You have drawn the letters:")
    print(', '.join(letters))

def display_game_instructions():
    print("Please input your submission for the longest anagram you can come up with")

def display_needs_valid_input_message():
    print("You entered in a word that contains characters not in the letter bank")
    display_game_instructions()

def display_needs_valid_input_message_2():
    print("You entered in a word that contains characters not in the letter bank or is not in the English dictionary")
    display_game_instructions()

def display_score(score):
    print(f"Your submitted anagram scored {score} points")

def display_retry_instructions():
    print("Should we play another round?")
    print("Enter y to replay")


def display_goodbye_message():
    print("Goodbye!")

# word_score must be a data structure such as a list or tuple where the first element
# is the word and the second element is the score.
def display_highest_score(word_score):
    print("Thanks for playing Adagrams!")
    print(f"The highest score from this game was {word_score[0]}, which was worth {word_score[1]} points.")