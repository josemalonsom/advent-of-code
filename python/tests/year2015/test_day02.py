import pytest

from tests.helper import get_file
from year2015.day02 import solve

class TestDay02:

    @pytest.mark.parametrize("puzzle_input, expected_wrapping_paper, expected_ribbon", [
        (["2x3x4"], 58, 34),
        (["1x1x10"], 43, 14)
    ])
    def test_wrapping_paper_examples(self, puzzle_input, expected_wrapping_paper, expected_ribbon):
        result = solve(puzzle_input)

        assert result["total_square_feet_of_wrapping_paper"] == expected_wrapping_paper
        assert result["total_ribbon_length"] == expected_ribbon

    def test_puzzle(self):
        puzzle_input = get_file("data.year2015", "day02-input.txt").readlines()
        result = solve(puzzle_input)

        assert result["total_square_feet_of_wrapping_paper"] == 1606483
        assert result["total_ribbon_length"] == 3842356
