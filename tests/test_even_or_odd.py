import pytest
from unittest.mock import patch
from io import StringIO
from src.even_or_odd import even_or_odd, print_is_even_or_odd

class TestEvenOrOdd:
    @pytest.mark.parametrize(
        "input_value, expected", 
        [
            (1, "Odd"),
            (2, "Even"),
            (30,"Even"),
            (1001, "Odd"),
            (0, "Even"),
            (-1, "Odd"),
            (-2, "Even"),
            (10**6, "Even"),
            (10**6+1, "Odd")
        ],
    )
    def test_even_or_odd_valid(self, input_value, expected):
        assert even_or_odd(input_value) == expected 

class TestPrintIsEvenOrOdd:
    @patch("builtins.input", return_value="7")
    @patch("sys.stdout", new_callable=StringIO)
    def test_print_is_even_or_odd(self, mock_stdout, mock_input):
        print_is_even_or_odd()
        assert mock_stdout.getvalue().strip() == "The number 7 is Odd"

    
    @patch("builtins.input", return_value="a")
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):
        print_is_even_or_odd()
        assert mock_stdout.getvalue().strip() == "Invalid input. Please enter a integer."
