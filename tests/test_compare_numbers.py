import pytest
from unittest.mock import patch
from io import StringIO
from src.compare_numbers import compare_two_numbers, get_number


class TestGetNumber:
    @pytest.mark.parametrize(
        "input_value,expected",
        [
            ("42", 42.0),
            ("3.14", 3.14),
            ("-10", -10.0),
            ("0", 0.0),
            ("100.5", 100.5),
            ("-3.14", -3.14),
        ],
    )
    def test_get_number_parametrized_valid(self, input_value, expected):
        with patch("builtins.input", return_value=input_value):
            result = get_number("Test prompt: ")
            assert result == expected

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "abc",
            "",
            "@#$",
            "12.34.56",
            "1 2 3",
            "hello world",
            "12abc",
        ],
    )
    def test_get_number_parametrized_invalid(self, invalid_input):
        """Pruebas parametrizadas para entradas inválidas"""
        with patch("builtins.input", return_value=invalid_input):
            with pytest.raises(ValueError, match="Please insert a valid number"):
                get_number("Test prompt: ")


class TestCompareTwoNumbers:
    @pytest.mark.parametrize(
        "num1,num2,expected",
        [
            (10.0, 5.0, "10.0 is bigger than 5.0"),
            (3.0, 8.0, "8.0 is bigger than 3.0"),
            (7.0, 7.0, "The numbers are equal: 7.0"),
            (-5.0, -10.0, "-5.0 is bigger than -10.0"),
            (0.0, 0.0, "The numbers are equal: 0.0"),
            (3.14, 2.71, "3.14 is bigger than 2.71"),
            (-3.0, 2.0, "2.0 is bigger than -3.0"),
            (0.0, 5.0, "5.0 is bigger than 0.0"),
            (0.0, -3.0, "0.0 is bigger than -3.0"),
            (100.5, 100.4, "100.5 is bigger than 100.4"),
        ],
    )
    def test_compare_two_numbers_parametrized(self, num1, num2, expected):
        result = compare_two_numbers(num1, num2)
        assert result == expected


class TestEdgeCases:
    def test_very_large_numbers(self):
        result = compare_two_numbers(1e10, 1e9)
        assert result == "10000000000.0 is bigger than 1000000000.0"

    def test_very_small_numbers(self):
        result = compare_two_numbers(0.0001, 0.0002)
        assert result == "0.0002 is bigger than 0.0001"

    def test_scientific_notation(self):
        result = compare_two_numbers(1e-5, 2e-5)
        assert result == "2e-05 is bigger than 1e-05"


class TestMainFlow:
    @patch("builtins.input", side_effect=["10", "5"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_flow_first_bigger(self, mock_stdout, mock_input):
        number_1 = get_number("Insert first number: ")
        number_2 = get_number("Insert second number: ")
        print(compare_two_numbers(number_1, number_2))
        output = mock_stdout.getvalue().strip()
        assert output == "10.0 is bigger than 5.0"

    @patch("builtins.input", side_effect=["7", "7"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_flow_equal_numbers(self, mock_stdout, mock_input):
        number_1 = get_number("Insert first number: ")
        number_2 = get_number("Insert second number: ")
        print(compare_two_numbers(number_1, number_2))
        output = mock_stdout.getvalue().strip()
        assert output == "The numbers are equal: 7.0"
