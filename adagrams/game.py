import random
def draw_letters():
    #creating a dictionary of letter pool
    letter_bank = {'A':9, 'B':2, 'C':2, 'D': 4, 'E': 12, 'F': 2, 'G':3, 'H': 2, 'I': 9, 'J': 1, 'K':1, 'L':4, 'M': 2, 'N':6, 'O': 8, 'P':2, 'Q':1, 'R': 6, 'S': 4, 'T':6, 'U':4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z':1}
    
    #get all of all possible letters
    tile_bag = []
    for letter, freq in letter_bank.items():
        for each_letter in range(freq):
            tile_bag.append(letter)

    #creates ten tiles from string from the list of letters
    tile_list = []
    for ten_letters in range(10):
        letter = random.choice(tile_bag)
        tile_list.append(letter)
        tile_bag.remove(letter)

    return tile_list
   

def uses_available_letters(word, letter_bank):
    #verifies if word is in letterbank and if there are enough tiles
    letter_list = [letter for letter in letter_bank if letter in word]
    if len(letter_list) == len(word):
        return True
    return False
  

def score_word(word):
    #creates empty variable for total/makes input all upper case
    total=0
    modified_word=word.upper()
    #Creates tile scores
    value1=["A","E","I","O","U","L","N", "R", "S", "T"]
    value_2=["D", "G"]
    value_3=["B", "C", "M", "P"]
    value_4=["F", "H", "V", "W", "Y"]
    value_5=["K"]
    value_8=["J", "X"]
    value_10=["Q", "Z"]

    #Assigns score for each letter in word, and gets total updating it 
    for letter in modified_word:
        if letter in value1:
            total+=1
        elif letter in value_2:
            total+=2
        elif letter in value_3:
            total+=3
        elif letter in value_4:
            total+=4
        elif letter in value_5:
            total+=5
        elif letter in value_8:
            total+=8
        elif letter in value_10:
            total+=10 
    if len(modified_word)>=7:
        total+=8
    return(total)

def get_highest_word_score(word_list):
    #Get word dictionary with words and point value
    word_dict = {}
    for word in word_list:
        word_dict[word] = score_word(word) 

   #gets the max value in dictionary
    max_value = max(word_dict.values())
    #get duplicates if present
    max_values = [k for k, v in word_dict.items() if v == max_value]
    #gets min word length
    min_word_length = min(len(k) for k, v in word_dict.items())
    #gets name of the max key 
    max_key = max(word_dict, key=word_dict.get)

    if len(max_values) > 1:
        #loopping over dictionary to find tie breaking winner
        tie_breaker = []
        for word , points in word_dict.items():
          #if ever see word with 10 instant winner 
          if len(word) == 10:
            tie_breaker = (word, points)
            return tie_breaker
          #if if there is no word with 10 it will print the word with the fewest letters
          elif len(word) == min_word_length:
              tie_breaker = (word, points)   
        return tie_breaker
    # if no duplicates print single winner 
    else:
      return max_key, word_dict[max_key]    
  