import pytest
from unittest.mock import patch
from io import StringIO
from src.vowels import is_a_vowel, print_is_a_vowel


class TestIsAVowel:
    @pytest.mark.parametrize("vowel", ["a", "e", "i", "o", "u"])
    def test_all_vowels_true(self, vowel):
        assert is_a_vowel(vowel) == True

    @pytest.mark.parametrize("vowel", ["b", "d", "f", "g", "h"])
    def test_consonants_false(self, vowel):
        assert is_a_vowel(vowel) == False

    @pytest.mark.parametrize("vowel", ["A", "B", "C", "D", "E"])
    def test_invalid_values(self, vowel):
        assert is_a_vowel(vowel) == False


class TestPrintIsAVowel:
    @patch("builtins.input", return_value="a")
    def test_print_with_value_a(self, mock_input, capsys):
        print_is_a_vowel()
        captured = capsys.readouterr()
        assert captured.out == "Is a vowel\n"

    @patch("builtins.input", return_value="b")
    def test_print_with_value_b(self, mock_input, capsys):
        print_is_a_vowel()
        captured = capsys.readouterr()
        assert captured.out == "Is not a vowel\n"

    @patch("builtins.input", return_value="A")
    def test_print_with_value_A(self, mock_input, capsys):
        print_is_a_vowel()
        captured = capsys.readouterr()
        assert captured.out == "Is not a vowel\n"
