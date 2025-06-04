from pprint import pprint

from input import input_centre_letter, input_outer_letters
from solver import solve, get_valid_word_count
from utils import create_word_list


def main():
    """
    Main function to run the word game solver.
    Prompts the user for input and displays the results.
    """
    create_word_list()

    centre_letter = input_centre_letter()
    outer_letters = input_outer_letters()

    valid_words = solve(centre_letter, outer_letters)
    valid_word_count = get_valid_word_count(set(valid_words))

    print(f"Valid words found: {valid_word_count}")
    print("Words:")

    pprint(valid_words)


if __name__ == "__main__":
    main()
