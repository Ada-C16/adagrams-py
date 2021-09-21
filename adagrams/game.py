#need to import the random package
import random

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

def draw_letters():
    #initialize a return_list variable
    return_list = []
    letter_freq = {}
    counter = 0
    #we change it to a while loop to return ten random letters and their values.
    while counter < 10:
        #choose an integer position random between 1 and 26
        #add LETTER_POOL[random int] to return_list
        #try:
            random_letter_index = random.randint(0,25)
            #Then, grab just the keys of the dictionary
            #And convert those to a list.
            #Then grab the index of that list using the random_letter number (1-26)
            #Because lists are 0-based, we need to subtract 1 otherwise we grab the letter before
            #the one we expect to grab.
            random_letter_val = list(LETTER_POOL.keys())[random_letter_index]

            #Before appending the random letter, we need to look up and make sure
            #it is not appearing more than the value in LETTER_POOL
            if random_letter_val in letter_freq:
                letter_freq[random_letter_val] += 1
            else:
                letter_freq[random_letter_val] = 1

            if letter_freq[random_letter_val] <= LETTER_POOL[random_letter_val]:
                return_list.append(random_letter_val)
                counter += 1

        #except Exception as e:
            #print(f"exception:{str(e)}")

    return return_list
    


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass