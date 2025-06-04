from src.solver import find_valid_combos, find_valid_words, solve, get_valid_word_count


class TestValidCombos:
    def test_valid_combos_is_list(self):
        test_centre_letter = "a"
        test_outer_letters = ["b", "c", "d", "e", "f", "g", "h", "i"]
        result = find_valid_combos(test_centre_letter, test_outer_letters)
        assert isinstance(result, list), "find_valid_combos should return a list."

    def test_valid_combos_contains_combos(self):
        test_centre_letter = "a"
        test_outer_letters = ["b", "c", "d", "e", "f", "g", "h", "i"]
        result = find_valid_combos(test_centre_letter, test_outer_letters)
        assert all(
            isinstance(combo, tuple) for combo in result
        ), "All items in the result should be tuples."

    def test_valid_combos_contains_centre_letter(self):
        test_centre_letter = "a"
        test_outer_letters = ["b", "c", "d", "e", "f", "g", "h", "i"]
        result = find_valid_combos(test_centre_letter, test_outer_letters)
        assert all(
            test_centre_letter in combo for combo in result
        ), "All combinations should contain the centre letter."

    def test_valid_combos_length(self):
        test_centre_letter = "a"
        test_outer_letters = ["b", "c", "d", "e", "f", "g", "h", "i"]
        result = find_valid_combos(test_centre_letter, test_outer_letters)
        assert all(
            4 <= len(combo) <= 9 for combo in result
        ), "All combinations should be between 4 and 9 letters long."


class TestValidWords:
    def test_valid_words_is_set(self):
        test_combos = [
            ("d", "o", "g"),
            ("c", "a", "t"),
            ("r", "a", "t"),
            ("b", "a", "t"),
        ]
        test_dictionary = {"dog", "cat", "bat", "rat"}
        result = find_valid_words(test_combos, test_dictionary)
        assert isinstance(
            result, set
        ), "find_valid_words should return a set of valid words."

    def test_valid_words_count(self):
        test_combos = [
            ("d", "o", "g"),
            ("c", "a", "t"),
            ("r", "a", "t"),
            ("b", "a", "t"),
        ]
        test_dictionary = {"dog", "cat", "bat", "rat"}
        test_words = find_valid_words(test_combos, test_dictionary)
        result = get_valid_word_count(test_words)
        assert (
            result == 4
        ), "find_valid_words should return correct amount of valid words."

    def test_valid_words_count_mismatch(self):
        test_combos = [
            ("d", "o", "g"),
            ("c", "t", "a"),
            ("r", "a", "t"),
            ("b", "a", "t"),
            ("b", "a", "t", "c", "h"),
        ]
        test_dictionary = {"dog", "cat", "bat", "rat", "xylophone"}
        test_words = find_valid_words(test_combos, test_dictionary)
        result = get_valid_word_count(test_words)
        assert (
            result == 4
        ), "find_valid_words should return correct amount of valid words."


class TestSolve:
    def test_solve_returns_list(self):
        centre_letter = "a"
        outer_letters = ["b", "c", "d", "e", "f", "g", "h", "i"]
        result = solve(centre_letter, outer_letters)
        assert isinstance(result, list), "solve should return a list of valid words."
