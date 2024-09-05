import pytest

from tests.helper import get_file
from year2015.day01 import solve

class TestDay01:

    @pytest.mark.parametrize("puzzle_input, expected_result", [
        ("(())", 0),
        ("(()(()(", 3),
        (")())())", -3)
    ])
    def test_floor_examples(self, puzzle_input, expected_result):
        assert solve(puzzle_input)["current_floor"] == expected_result

    @pytest.mark.parametrize("puzzle_input, expected_result", [
        (")", 1),
        ("()())", 5)
    ])
    def test_character_taking_to_basement(self, puzzle_input, expected_result):
        assert solve(puzzle_input)["position_character_taking_to_basement"] == expected_result

    def test_puzzle(self):
        puzzle_input = get_file("data.year2015", "day01-input.txt").read()
        result = solve(puzzle_input)

        assert result["current_floor"] == 74
        assert result["position_character_taking_to_basement"] == 1795
