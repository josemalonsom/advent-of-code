import pytest

from year2015.day04 import solve_puzzle


class TestDay04:

    @pytest.mark.parametrize("puzzle_input, expected_answer", [
        ("abcdef", 609043),
        ("pqrstuv", 1048970)
    ])
    def test_examples_puzzle_1(self, puzzle_input, expected_answer):
        result = solve_puzzle(puzzle_input)

        assert result["answer"] == expected_answer

    def test_puzzle_five_zeroes(self):
        result = solve_puzzle("ckczppom")

        assert result["answer"] == 117946

    def test_puzzle_six_zeroes(self):
        result = solve_puzzle("ckczppom", 6)

        assert result["answer"] == 3938038
