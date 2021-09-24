import random

def draw_letters():

    letter_list = ['A','A','A','A','A','A','A','A','A','B','B', 
    'C', 'C', 'D', 'D', 'D','D','E','E','E','E','E','E','E','E',
    'E','E','E','E','F','F','G','G','G','H','H','I','I','I', 
    'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M',
     'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T',
      'T','T','T','T','T', 'U', 'U', 'U', 'U', 'V', 'V', 'W','W', 'X', 'Y','Y','Z']
    letters = letter_list.copy()
    chosen_letters = []
    for i in range(10):
        letter = random.choice(letters)
        letters.remove(letter)
        chosen_letters.append(letter)
    return chosen_letters
        
def uses_available_letters(word, letter_bank):

    letters_used = letter_bank.copy()
    for letter in word:
        if letter in letters_used:
            letters_used.remove(letter)
        else:
            return False
            break
    return True    

def score_word(word):

    letter_points = {
            1:['A', 'E', 'I','O', 'U', 'L', 'N', 'R', 'S', 'T' ],
            2:['D', 'G' ], 
            3:['B', 'C', 'M', 'P' ],
            4:['F', 'H', 'V', 'W', 'Y' ],
            5:['K'],
            8:['J', 'X'],
            10:['Q', 'Z']
        }
    sum = 0
    word_length = len(word)
    cap_word = word.upper()
    for letter in cap_word:
        for score in letter_points:
            if letter in letter_points[score]:
                sum += score
    if word_length >= 7:
        sum += 8  
    return sum

def get_highest_word_score(word_list):
    words_and_scores = []
    for word in word_list:
        score = score_word(word)
        words_and_scores.append(tuple([word, score]))
    num=(0, 0)
    for item in words_and_scores:
        if item[1]>num[1]:
            num=item
        elif item[1]==num[1]: 
            if len(num[0])==10:
                break
            elif len(item[0])==len(num[0]):
                break
            elif len(item[0])==10:
                num=item
                break
            elif len(item[0])<len(num[0]):
                num=item
    return num