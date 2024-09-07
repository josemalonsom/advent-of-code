import pytest

from tests.helper import get_file
from year2015.day03 import solve_puzzle_1, solve_puzzle_2

class TestDay03:

    @pytest.mark.parametrize("puzzle_input, expected_houses", [
        (">", 2),
        ("^>v<", 4),
        ("^v^v^v^v^v", 2),
    ])
    def test_examples_puzzle_1(self, puzzle_input, expected_houses):
        result = solve_puzzle_1(puzzle_input)

        assert result["total_houses_receiving_presents"] == expected_houses

    def test_puzzle_1(self):
        puzzle_input = get_file("data.year2015", "day03-input.txt").read()
        result = solve_puzzle_1(puzzle_input)

        assert result["total_houses_receiving_presents"] == 2081

    @pytest.mark.parametrize("puzzle_input, expected_houses", [
        ("^v", 3),
        ("^>v<", 3),
        ("^v^v^v^v^v", 11),
    ])
    def test_examples_puzzle_2(self, puzzle_input, expected_houses):
        result = solve_puzzle_2(puzzle_input)

        assert result["total_houses_receiving_presents"] == expected_houses

    def test_puzzle_2(self):
        puzzle_input = get_file("data.year2015", "day03-input.txt").read()
        result = solve_puzzle_2(puzzle_input)

        assert result["total_houses_receiving_presents"] == 2341