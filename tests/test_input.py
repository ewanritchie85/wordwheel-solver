import pytest

from src.input import input_centre_letter, input_outer_letters


class TestCentreLetterInput:
    def test_input_centre_letter(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "a")
        assert input_centre_letter() == "a"

    def test_input_centre_letter_with_spaces(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: " a ")
        assert input_centre_letter() == "a"

    def test_input_centre_letter_lowercase(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "A")
        assert input_centre_letter() == "a"

    def test_input_centre_letter_invalid(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "1")
        with pytest.raises(ValueError):
            input_centre_letter()


class TestOuterLettersInput:
    def test_input_outer_letters(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "abcdefg")
        assert input_outer_letters() == ["a", "b", "c", "d", "e", "f", "g"]

    def test_input_outer_letters_with_spaces(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: " a b c d e f g ")
        assert input_outer_letters() == ["a", "b", "c", "d", "e", "f", "g"]

    def test_input_outer_letters_lowercase(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "ABCDEFG")
        assert input_outer_letters() == ["a", "b", "c", "d", "e", "f", "g"]

    def test_input_outer_letters_invalid_length(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "abcde")
        with pytest.raises(ValueError):
            input_outer_letters()

    def test_input_outer_letters_invalid_characters(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "abc1efg")
        with pytest.raises(ValueError):
            input_outer_letters()
