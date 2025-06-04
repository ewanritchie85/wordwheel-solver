def centre_letter_input() -> str:
    """
    Prompts the user to input a single letter that will be the centre letter of the game.

    Args:
        n/a

    Returns:
        str: The centre letter input by the user.
    """
    centre_letter = (
        input("Please enter a single letter to be the centre letter: ").strip().lower()
    )
    return centre_letter


def outer_letters_input() -> list:
    """
    Prompts the user to input a list of letters that will be the outer letters of the game.

    Args:
        n/a

    Returns:
        list: A list of letters input by the user.
    """
    outer_letters = (
        input("Please enter 7 letters to be the outer letters: ").strip().lower()
    )
    outer_letters_list = []
    outer_letters_list.extend(outer_letters)

    return outer_letters_list
