import pytest

from src.solver import valid_combos

class TestValidCombos:
    def test_valid_combos_is_list(self):
        test_centre_letter = "a"
        test_outer_letters = ["b", "c", "d", "e", "f", "g", "h", "i"]
        result = valid_combos(test_centre_letter, test_outer_letters)
        assert isinstance(result, list), "Solver should return a list."
    
    def test_valid_combos_contains_combos(self):
        test_centre_letter = "a"
        test_outer_letters = ["b", "c", "d", "e", "f", "g", "h", "i"]
        result = valid_combos(test_centre_letter, test_outer_letters)
        assert all(isinstance(combo, tuple) for combo in result), "All items in the result should be tuples."
        
    def test_valid_combos_contains_centre_letter(self):
        test_centre_letter = "a"
        test_outer_letters = ["b", "c", "d", "e", "f", "g", "h", "i"]
        result = valid_combos(test_centre_letter, test_outer_letters)
        assert all(test_centre_letter in combo for combo in result), "All combinations should contain the centre letter."
        
    def test_valid_combos_length(self):
        test_centre_letter = "a"
        test_outer_letters = ["b", "c", "d", "e", "f", "g", "h", "i"]
        result = valid_combos(test_centre_letter, test_outer_letters)
        assert all(4 <= len(combo) <= 9 for combo in result), "All combinations should be between 4 and 9 letters long."