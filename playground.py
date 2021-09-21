import  random
# Psuedocode
    # 1. convert dictionary to a list of all letters with all frequence
        # for key["A"] 
        #     frequence = key[value]
        # for key value range(frequency):
        #     list.Append(key)
    #2. Randomly select 10 letters from master letter list and put in letters list
        # remove letter from master letter list
    #3. return letters

def convert_letter_dictionary_to_list(letters):
    letter_list = []
    frequency = 0
    
    for key, object in letters.items():
        frequency = object
        for i in range(frequency):
            letter_list.append(key)
    return letter_list

def draw_letters():
    user_hand = []
    principle_letter_list = convert_letter_dictionary_to_list(LETTER_POOL)
    for letter in range(10):
        letter_to_add = principle_letter_list[random.randint(0, len(principle_letter_list))]
        user_hand.append(letter_to_add)
        principle_letter_list.remove(letter_to_add)
    return user_hand

def test_draw_letters_draws_ten():
    # Arrange/Act
    letters = draw_letters()

    # Assert
    assert len(letters) == 10
