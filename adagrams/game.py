import random


def draw_letters():
    letter_pile = "".join([
        "A"*9,
        "B"*2,
        "C"*2,
        "D"*4,
        "E"*12,
        "F"*2,
        "G"*3,
        "H"*2,
        "I"*9,
        "J"*1,
        "K"*1,
        "L"*4,
        "M"*2,
        "N"*6,
        "O"*8,
        "P"*2,
        "Q"*1,
        "R"*6,
        "S"*4,
        "T"*6,
        "U"*4,
        "V"*2,
        "W"*2,
        "X"*1,
        "Y"*2,
        "Z"*1,
    ])

    hand = list()
    while len(hand) < 10:
        draw = random.choice(letter_pile)
        if hand.count(draw) >= letter_pile.count(draw):
            continue # too many of this letter, pick another
        hand.append(draw)
    return hand


def uses_available_letters(word, hand):
    # challenge accepted
    return all([word.count(letter) <= hand.count(letter) for letter in set(word)])


def score_word(word):

    score_chart = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"],
    }

    word = word.upper()
    points = 0
    for key, value in score_chart.items():
        for letter in value:
            count = word.count(letter)
            points += key * count

    if len(word) in range(7, 11):
        points += 8
    return points


def get_highest_word_score(word_list):
    word_scores = {word: score_word(word) for word in word_list}
    high_score = max(word_scores.values())
    ties = [w for w in word_scores.keys() if word_scores[w] == high_score]

    shortest = ties[0]
    for word in ties:
        if len(word) == 10:
            return word, high_score
        if len(word) < len(shortest):
            shortest = word

    return shortest, high_score
