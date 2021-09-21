# Project notes
We can put notes here on the tests, or future strategies to try...

# Wave 1
- Tests one function: `draw_letters()`
- Must draw letters with probability matching the letter distribution
- IMO it's impossible to truly test for probability, so this will probably be evaluated when we turn the project in and not at the test stage. I suspect this also means we could pass the tests but still not have written the function correctly.  It looks like the tests will check whether a letter can be drawn too many times but not if the frequency of a letter being drawn matches the intended probability.
- It seems like there are many ways to approach the probability pool for drawing letters...but what is the best way?
- README says depending on method this could be easy or difficult. I was thinking of a copy of the letter/quantity dict so that we don't change the original. But not sure if we'd need to do a deepcopy since it's a dict.  

# Wave 2
- Tests `uses_available_letters(word, letter_bank)`
- This function is a check on whether the user has submitted word that uses only the letters they were dealt
- Looking at these tests answers one thing that was confusing me--the anagram the user submits doesn't have to use all 10 of the letters they are given
- `letter_bank` is a list, but according to the tests we should be sure not to mutate it
- Trying to think up a conditional that will see how many letters in the input word are in the letterbank...might be useful to draw out/visualize.

# Wave 3
- Tests the `score_word(word)` function
- Assigns a score based on the letters in the word and the length of the word 
- Acording to the tests, we should score an empty string as zero
- According to the tests, we should ignore whether the input is upper or lower case
  
# Wave 4
- Tests the `get_highest_score(word_list)` function
- Basically, gets a list of words and decides which is the highest scoring one