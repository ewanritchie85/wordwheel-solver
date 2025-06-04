import sys
from input import input_centre_letter, input_outer_letters
from solver import solve, get_valid_word_count


def main():
    """
    Main function to run the word game solver.
    Prompts the user for input and displays the results.
    """

    while True:
        try:
            centre_letter = input_centre_letter()
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            outer_letters = input_outer_letters()
            break
        except ValueError as e:
            print(e)

    valid_words = solve(centre_letter, outer_letters)
    valid_word_count = get_valid_word_count(set(valid_words))

    print(f"Valid words found: {valid_word_count}")
    print("Words:")

    print(valid_words)
    
    while True:
        choice = input("Press 'x' to exit: ").strip().lower()
        if choice == 'x':
            print("Goodbye")
            break
        print("Invalid input. Please press 'x' to exit.")


if __name__ == "__main__":
    main()
