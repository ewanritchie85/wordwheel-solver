from itertools import permutations, combinations

from src.input import input_centre_letter, input_outer_letters


def valid_combos(centre_letter: str, outer_letters: list):
    matching_words = []
    letters = [centre_letter] + outer_letters
    for i in range(4, 10):
        letter_combos = list(combinations(letters, i))
        for combo in letter_combos:
            if centre_letter in combo:
                matching_words.append(combo)

    print(matching_words)

    return matching_words
