import os
import pytest

from src.utils import create_word_list


@pytest.fixture(scope="function")
def fresh_word_list():
    create_word_list()
    yield


def get_word_list():
    """
    Helper function to read the word list from the file.

    Returns:
        list: A list of words from the word list file.
    """
    with open("./data/word_list.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


@pytest.mark.usefixtures("fresh_word_list")
class TestCreateWordList:
    def test_word_list_exists(self):
        """
        Test that the word list file exists.
        """
        assert os.path.exists("./data/word_list.txt"), "Word list file does not exist."

    def test_word_list_lengths(self):
        """
        Test that the word list contains words of lengths 4 to 9.
        """
        for word in get_word_list():
            word = word.strip()
            assert (
                4 <= len(word) <= 9
            ), f"Word '{word}' is not between 4 and 9 characters long."

    def test_word_list_lower_case(self):
        """
        Test that all words in the word list are in lower case.
        """
        for word in get_word_list():
            word = word.strip()
            assert word.islower(), f"Word '{word}' is not in lower case."
