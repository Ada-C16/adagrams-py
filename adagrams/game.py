def draw_letters():
    pass

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