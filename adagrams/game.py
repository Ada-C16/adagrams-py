import random


def draw_letters():
    letter_dict = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1,
    }

    letter_qty = [key * value for key, value in letter_dict.items()]
    letter_split = [c for i in letter_qty for c in i]

    # works but is kinda ugly make hot if possible
    letter_bank = list()
    while len(letter_bank) < 10:
        draw = random.choice(letter_split)
        if letter_bank.count(draw) >= letter_dict[draw]:
            continue
        letter_bank.append(draw)
    return letter_bank


def uses_available_letters(word, letter_bank):
    # works. beautiful & perfect
    bank_dict = {letter: letter_bank.count(letter) for letter in letter_bank}

    # lain will probably try to make this hotter.
    for letter in word:
        if bank_dict.get(letter):
            bank_dict[letter] -= 1
        else:
            return False
    return True


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
    # not finished doesnt account for tie
    # but look at that sweet little lamb(da)

    # word_scores = {word: score_word(word) for word in word_list}
    # winner = max(word_scores.items(), key=lambda kv: kv[1])

    word_scores = {}
    for word in word_list:
        score = score_word(word)
        if not word_scores.get(score):
            word_scores[score] = [word]
        else:
            word_scores[score].append(word)
    ties = word_scores[max(word_scores, key=word_scores.get)]
    shortest = ""
    for word in ties:
        if len(word) == 10:
            return word
        if len(word) < len(shortest):
            shortest = word
        if len(word) == len(shortest):
            pass
    return shortest
