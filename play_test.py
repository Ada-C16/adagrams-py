# def score_word(word):

#     # Create points collectio
#     sample = {
#         1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S'],
#         2: ['D', 'G'],
#         3: ['B', 'C', 'M', 'P'],
#         4: ['F', 'H', 'V', 'W', 'Y'],
#         5: ['K'],
#         8: ['J', 'X'],
#         10: ['Q', 'Z']
#     }

# #     return score
# sample = {
#         ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S'): 1,
#         ('D', 'G'): 2,
#         ('B', 'C', 'M', 'P'): 3,
#         ('F', 'H', 'V', 'W', 'Y'): 4,
#         ('K'): 5,
#         ('J', 'X'): 8,
#         ('Q', 'Z'): 10
#     }

# print(sample[1])




def score_word(word):

    score = 0

    # list of lists
    scores = [
            ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S'], # 1
            ['D', 'G'], # 2
            ['B', 'C', 'M', 'P'], # 3
            ['F', 'H', 'V', 'W', 'Y'], #4
            ['K'], #5
            ['J', 'X'],  #8
            ['Q', 'Z'], #10
    ]

    for letter in word:
        letter = letter.upper()
        if letter in scores[0]:
            score += 1
        elif letter in scores[1]:
            score += 2
        elif letter in scores[2]:
            score += 3
        elif letter in scores[3]:
            score += 4
        elif letter in scores[4]:
            score += 5
        elif letter in scores[5]:
            score += 8
        elif letter in scores[6]:
            score += 10

    if 7 <= len(word) <= 10:
        score += 8

    return score

words = ["BBBBBB", "AAAAAAAAAA"]

# def get_highest_word_score(word_list):
    
#     words_scores_dict = {}

#     # Score words and store in words_scores_dict
#     for word in word_list:
#         words_scores_dict[word] = score_word(word)
    
#     # Find highest scores
#     highest = max(words_scores_dict.values())
    
#     highest_values = [k for k, v in words_scores_dict.items() if v == highest]
#     # ['BBBBBB', 'AAAAAAAAAA']
#     print(f'{highest_values=}')

#     # Determine list of lengths
#     highest_words_by_length = []
#     if len(highest_values) > 1:
#         for word in highest_values:
#             highest_words_by_length.append(len(word))

    # Then return (word, score) for first 10 letter word if exits or first, shortest word
    ############# WAVE 4.02
def get_highest_word_score(word_list):

    highest_word = ("", 0)
    for word in word_list:
        if score_word(word) >= highest_word[1]:
            if len(word) == 10:
                highest_word = (word,score_word(word))
                return highest_word
            elif len(word) < highest_word[1]:
                highest_word = (word,score_word(word))
                return highest_word
            elif len(word) == highest_word[0] and score_word(word) == highest_word[1]:
                return "cat"




    #########################################################################

        # # Account for 10 letter
        # for word in highest_values:
        #     length = len(word)
        #     if len(word) == 10:
        #         return (highest_values[0], words_scores_dict[highest_values[0]]) 
        #     elif len(word) < 10:
        #         shorter_word = min(highest_values, key=len)
        #         return (shorter_word, words_scores_dict[shorter_word])
    ########################################################################3
    else:
        return (highest_values[0], words_scores_dict[highest_values[0]])
    
    
    

    # return (max_score_word, score_word(max_score_word))
    


best_word = get_highest_word_score(words)
print(best_word)



# X - score words
# X - find highest word scores
    # X - put high scores in list
# X - If only one score, return
# If there is a tie
    # Return first 10 letter word
    # First shortest word is winner
        # min()?
        # # Between two words of equal length, first word wins
        # # Between two words of diff length, shorter word wins
    

[3, 3, 5, 7, 8]