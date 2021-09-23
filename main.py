import sys
from adagrams.ui_helper import *
from adagrams.game import *

def wave_1_run_game():
    display_welcome_message()
    game_continue = True
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
    
        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
   
    display_goodbye_message()

def wave_2_run_game():
    display_welcome_message()
    game_continue = True
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
        user_input_word = input()

        while( not uses_available_letters(user_input_word, letter_bank)):
            display_needs_valid_input_message()
            user_input_word = input()

        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
   
    display_goodbye_message()

def wave_3_run_game():
    display_welcome_message()
    game_continue = True
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
        user_input_word = input()

        while( not uses_available_letters(user_input_word, letter_bank)):
            display_needs_valid_input_message()
            user_input_word = input()
        
        score = score_word(user_input_word)
        display_score(score)

        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
    display_goodbye_message()

def wave_4_run_game():
    display_welcome_message()
    game_continue = True
    played_words = []
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
        user_input_word = input()

        while( not uses_available_letters(user_input_word, letter_bank)):
            display_needs_valid_input_message()
            user_input_word = input()
        
        score = score_word(user_input_word)
        display_score(score)
        played_words.append(user_input_word)

        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
    display_highest_score(get_highest_word_score(played_words))
    display_goodbye_message()

def wave_5_run_game():
    display_welcome_message()
    print("\nType 9 to quit game at any time.")
    game_continue = True
    played_words = []
    while game_continue:
        print("\nLet's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
        user_input_word = get_valid_word_from_user()

        while (not uses_available_letters(user_input_word, letter_bank)) or checks_user_word_in_dictionary(user_input_word) == False:
            if not uses_available_letters(user_input_word, letter_bank):
                display_needs_valid_input_message()
                user_input_word = get_valid_word_from_user()
            else:
                display_needs_word_in_dictionary_message()
                user_input_word = get_valid_word_from_user()

        score = score_word(user_input_word)
        display_score(score)
        all_possible = finds_all_possible_words_with_scores(letter_bank)
        best_score, best_words = gets_best_possible(all_possible)
        print(f"The best possible word(s): {best_words} with a score of {best_score}.")
        played_words.append(user_input_word)

        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input.lower() == "y"
    display_highest_score(get_highest_word_score(played_words))
    display_goodbye_message()

def main(wave):
    if(wave == 1):
        wave_1_run_game()
    elif(wave == 2):
        wave_2_run_game()
    elif(wave == 3):
        wave_3_run_game()
    elif(wave == 4):
        wave_4_run_game()
    elif(wave == 5):
        wave_5_run_game()
    else:
        print("Please input a wave number.  Valid wave numbers are 1, 2, 3, 4, 5.")

if __name__ == "__main__":
    args = sys.argv
    if(len(args) >= 2 and args[1].isnumeric()):
        wave = int(args[1])
    else:
        wave = "ERROR"
    main(wave)