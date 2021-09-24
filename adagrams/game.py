#Wave 1
def draw_letters():

  letters_list=[]
  import random
  letters_dict = {'A' : 9, 'N' : 6, 'B' : 2, 	'O' : 8,
'C' : 2, 	'P' : 2,
'D' : 4, 	'Q' : 1,
'E' : 12, 	'R' : 6,
'F' : 2, 	'S' : 4,
'G' : 3, 	'T' : 6,
'H' : 2, 	'U' : 4,
'I' : 9, 	'V' : 2,
'J' : 1, 	'W' : 2,
'K' : 1, 	'X' : 1,
'L' : 4, 	'Y' : 2,
'M' : 2, 	'Z' : 1}
  l=len(letters_list)
  for l in range (0,10):
    letter=random.choice(list(letters_dict.keys()))
    letter=letter.upper()
    letters_list.append(letter)
    for key,value in letters_dict.items():
      if letters_list.count(key) >= value:
        letters_list.remove(key)
        letter=random.choice(list(letters_dict.keys()))
        letter=letter.upper()
        letters_list.append(letter)
  return letters_list
  


# Wave 2
def available_letters_quantity(letter_bank):
    '''
    Creates a dictionary of letters and their amounts in the drawn hand.

    Parameter:
        letter_bank, a list of one-character strings

    Output:
        letters_amount, a dictionary; example: letters_amount = {'a': 3, 'f': 2, 'm': 1, 'x': 1, 'g': 2, 'e': 1}
    '''
    letters_amount = {}
    for letter in letter_bank:
        if letter not in letters_amount:
            letters_amount[letter] = 1
        else:
            letters_amount[letter] += 1
    return letters_amount
def uses_available_letters(word, letter_bank):
    '''
    Determines if the word entered by the player is an anagram of the player's drawn letters.

    Parameters: 
        word, a string
        letter_bank, a list of one-character strings
    
    Output:
        boolean, True or False
    '''
    letter_bank_dict = available_letters_quantity(letter_bank) 
    for letter in word:
        if letter in letter_bank_dict and letter_bank_dict[letter] > 0:
            letter_bank_dict[letter] -= 1
        else:
            return False
    return True

#Wave 3
def score_word(word):
    #word=string
    #Returns points(int)
    letter_dict={1:['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 2:['D','G'],3:['B', 'C', 'M', 'P' ],4:['F', 'H','V', 'W', 'Y'],5:['K'],8:['J','X'],10:['Q','Z']}
    sum=0
    
    for letter in word:
      for i in letter_dict.keys():
         if letter.upper() in letter_dict[i]:
           sum+=i
      
    if len(word) in range(7,11):
      sum+=8
    return sum

# Wave 4
def words_and_scores(word_list):
    '''
    Creates a dictionary where the key is a word that the user entered and the value is a dictionary of this word's attributes.

    Parameter:
        word_list, a list of strings representing the user-entered words.

    Output:
        words_and_scores_dict, a dictionary of dictionaries
        example: letters_amount = {"AAA":  {score: 3, "word_list_index": 0, "word_length": 3}, "EEE": {score: 3, "word_list_index": 1, "word_length": 3}}
    '''
    words_and_scores_dict = {}
    for i in range(len(word_list)):
        words_and_scores_dict[word_list[i]] = {"score": score_word(word_list[i]), "word_list_index": i, "word_length": len(word_list[i])}
    return words_and_scores_dict

def get_highest_word_score(word_list):
    '''
    Determines the highest scoring word and its score.

    Parameter:
        word_list, a list of strings representing the user-entered words.

    Output:
        Tuple, where tuple[0] is the highest scoring word and tuple[1] is the score
        Example: ('AAA', 3) 
    '''
    words_and_scores_dict = words_and_scores(word_list)
    highest_score = 0
    highest_scoring_word = None
    highest_scoring_word_index = None
    for word_key in words_and_scores_dict:
        score = words_and_scores_dict[word_key]["score"]
        index = words_and_scores_dict[word_key]["word_list_index"]
        length = words_and_scores_dict[word_key]["word_length"] 
        if score > highest_score:
            highest_score = score
            highest_scoring_word = word_key
            highest_scoring_word_index = index
        elif score == highest_score:
            if length == 10 and len(highest_scoring_word) != 10:
                    highest_score = score
                    highest_scoring_word = word_key
            elif length == len(highest_scoring_word):
                if index < highest_scoring_word_index:
                    highest_scoring_word = word_key
            elif length < len(highest_scoring_word) and len(highest_scoring_word) != 10:
                highest_scoring_word = word_key
    return highest_scoring_word, highest_score
