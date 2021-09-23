import random


def draw_letters():
    """
    Returns:
        hand (list): An array of ten random letters representing the users hand.
    """

    letter_pile = "".join(
        [
            "A" * 9,
            "B" * 2,
            "C" * 2,
            "D" * 4,
            "E" * 12,
            "F" * 2,
            "G" * 3,
            "H" * 2,
            "I" * 9,
            "J" * 1,
            "K" * 1,
            "L" * 4,
            "M" * 2,
            "N" * 6,
            "O" * 8,
            "P" * 2,
            "Q" * 1,
            "R" * 6,
            "S" * 4,
            "T" * 6,
            "U" * 4,
            "V" * 2,
            "W" * 2,
            "X" * 1,
            "Y" * 2,
            "Z" * 1,
        ]
    )
    return random.sample(letter_pile, 10)


def uses_available_letters(word, hand):
    """
    Returns:
        True if word uses only letters in users hand.
    """

    # sexy
    return all([word.count(letter) <= hand.count(letter) for letter in set(word)])


def score_word(word):
    """
    Returns:
        score (int): An integer representing the total score of word.
    """

    word = word.upper()
    score_chart = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"],
    }

    score = sum(
        [
            letter_points * word.count(letter)
            for letter_points, letters in score_chart.items()
            for letter in letters
        ]
    )
    if len(word) in range(7, 11):  # slurpee
        score += 8

    return score


def get_highest_word_score(word_list):
    """
    Returns:
        winning word, high_score (tuple): A tuple containing the winning word (str) and high score (int).
    """

    word_scores = {word: score_word(word) for word in word_list}
    high_score = max(word_scores.values())
    ties = [word for word, score in word_scores.items() if score == high_score]
    return tie_breaker(ties), high_score


def tie_breaker(ties):
    """
    Returns:
        word (str): A string containing the word with fewest letters earliest in sequence, or
        preferentailly a word with 10 letters.
    """
    # I do not approve of this -mac
    # neither do i - lain
    return next(filter(lambda w: len(w) == 10, ties), None) or min(ties, key=len)
