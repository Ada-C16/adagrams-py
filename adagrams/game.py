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
    This function creates a dictionary of letters and their amounts in the drawn hand.

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
    This function determines if the word entered by the player is an anagram of the player's drawn letters.

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
            print(letter_bank_dict)
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
      
    if len(word) in range(7,10):
      sum+=8
    return sum

# Wave 4
def words_and_scores(word_list):
    words_and_scores_dict = {}
    for i in range(len(word_list)):
        words_and_scores_dict[word_list[i]] = score_word(word_list[i])
    print(words_and_scores_dict)
    return words_and_scores_dict


def get_highest_word_score(word_list):
    words_and_scores_dict = words_and_scores(word_list)
    highest_score = 0
    highest_scoring_word = None
    for word, score in words_and_scores_dict.items():
        if score > highest_score:
            highest_score = score
            highest_scoring_word = word
        elif score == highest_score and len(word) == 10:
            highest_score = score
            highest_scoring_word = word
        elif score == highest_score and len(word) == len(highest_scoring_word):
            pass

    return highest_score, highest_scoring_word