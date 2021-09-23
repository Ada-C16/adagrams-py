import random

LETTER_PILE = "".join(
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

POINTS_CHART = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"],
}


def draw_letters():
    """
    Returns:
        hand (list): An array of ten random letters representing the users hand.
    """

    return random.sample(LETTER_PILE, 10)


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
    score = sum(
        [
            letter_points * word.count(letter)
            for letter_points, letter_list in POINTS_CHART.items()
            for letter in letter_list
        ]
    )
    if len(word) >= 7:
        score += 8
    return score


def get_highest_word_score(word_list):
    """
    Returns:
        winning word, high_score (tuple): A tuple containing the winning word (str) and high score (int).
    """
    words_by_score = dict()
    for word in word_list:
        words_by_score.setdefault(score_word(word), []).append(word)
    high_score = max(words_by_score)
    return tie_breaker(words_by_score[high_score]), high_score


def tie_breaker(ties):
    """
    Returns:
        word (str): A string containing the word with fewest letters earliest in sequence, or
        preferentailly a word with 10 letters.
    """
    # I do not approve of this -mac
    # neither do i - lain
    return next(filter(lambda w: len(w) == 10, ties), None) or min(ties, key=len)
