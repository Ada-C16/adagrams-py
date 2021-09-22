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
  


def uses_available_letters(word, letter_bank):
    pass

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


def get_highest_word_score(word_list):
    pass