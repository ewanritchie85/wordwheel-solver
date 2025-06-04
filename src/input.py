def input_centre_letter() -> str:
    """
    Prompts the user to input a single letter that will be the centre letter of the game.

    Args:
        n/a

    Returns:
        str: The centre letter input by the user.
    """
    centre_letter = (
        input("Please enter the central letter: ").strip().lower()
    )
    if centre_letter.isalpha() and len(centre_letter) == 1:
        return centre_letter
    else:
        raise ValueError(
            f"Invalid input: '{centre_letter}'. Please enter a single letter."
        )


def input_outer_letters() -> list:
    """
    Prompts the user to input a list of letters that will be the outer letters of the game.

    Args:
        n/a

    Returns:
        list: A list of letters input by the user.
    """
    outer_letters = (
        input("Please enter the eight outer letters: ").strip().lower()
    )
    outer_letters_list = []
    for letter in outer_letters:
        if letter.isalpha():
            outer_letters_list.append(letter)

    if len(outer_letters_list) == 8:
        return outer_letters_list
    else:
        raise ValueError(
            f"Invalid input: '{outer_letters}'. Please enter 8 letters."
        )
