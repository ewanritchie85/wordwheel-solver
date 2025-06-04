from itertools import permutations, combinations


def find_valid_combos(centre_letter: str, outer_letters: list) -> list[tuple]:
    """Finds all valid combinations of letters that include the centre letter and
    are between 4 and 9 letters long.

    Args:
        centre_letter (str): single letter from user input_centre_letter
        outer_letters (list): list of 8 letters from user input_outer_letters

    Returns:
        list: a list of all valid combinations of letters
    """
    valid_combos = []
    letters = [centre_letter] + outer_letters
    for i in range(4, 10):
        letter_combos = combinations(letters, i)
        for combo in letter_combos:
            if centre_letter in combo:
                valid_combos.append(combo)
    return valid_combos


def find_valid_words(combos: list[tuple], dictionary: set[str]) -> set[str]:
    """Finds all valid words from the provided combinations that exist in the dictionary.

    Args:
        combos (list[tuple]): output of find_valid_combos function
        dictionary (set[str]): set of words from word_list.txt

    Returns:
        set[str]: a set of valid word matches from the dictionary
    """
    valid_words = set()
    for combo in combos:
        for perm in permutations(combo):
            word = "".join(perm)
            if word in dictionary:
                valid_words.add(word)
    return valid_words


def solve(centre_letter: str, outer_letters: list[str]) -> list[str]:
    """Solves the word game by finding all valid words that can be formed

    Args:
        centre_letter (str): single letter from user input_centre_letter
        outer_letters (list): list of 8 letters from user input_outer_letters

    Returns:
        list[str]: alphabetically sorted list of valid words
    """
    combos = find_valid_combos(centre_letter, outer_letters)
    with open("./data/word_list.txt", "r", encoding="utf-8") as file:
        dictionary = set(word.strip().lower() for word in file)
    return sorted(find_valid_words(combos, dictionary))


def get_valid_word_count(valid_words: set[str]) -> int:
    """
    Returns the number of valid words in the provided set.

    Args:
        valid_words (set): A set of valid words.

    Returns:
        int: The count of valid words.
    """
    return len(valid_words)
