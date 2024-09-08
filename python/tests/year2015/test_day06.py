import pytest

from tests.helper import get_file
from year2015.day06 import solve_puzzle_1, solve_puzzle_2


class TestDay06:

    @pytest.mark.parametrize("puzzle_input, expected_answer", [
        (["toggle 0,0 through 2,2"], 9),
        (["toggle 0,0 through 999,999"], 1_000_000),
        (["turn on 0,0 through 999,999"], 1_000_000),
        (["toggle 0,0 through 999,0"], 1_000),
        (["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"], 999_996)
    ])
    def test_examples_puzzle_1(self, puzzle_input, expected_answer):
        result = solve_puzzle_1(puzzle_input)

        assert result["answer"] == expected_answer

    def test_puzzle_1(self):
        puzzle_input = get_file("data.year2015", "day06-input.txt").readlines()
        result = solve_puzzle_1(puzzle_input)

        assert result["answer"] == 543903

    @pytest.mark.parametrize("puzzle_input, expected_answer", [
        (["turn on 0,0 through 0,0"], 1),
        (["turn on 0,0 through 0,0", "turn on 0,0 through 0,0"], 2),
        (["turn on 0,0 through 0,0", "toggle 0,0 through 0,0"], 3),
        (["turn on 0,0 through 0,0", "turn off 0,0 through 0,0"], 0),
        (["turn off 0,0 through 0,0", "turn off 0,0 through 0,0"], 0),
        (["toggle 0,0 through 999,999"], 2_000_000)
    ])
    def test_examples_puzzle_2(self, puzzle_input, expected_answer):
        result = solve_puzzle_2(puzzle_input)

        assert result["answer"] == expected_answer

    def test_puzzle_2(self):
        puzzle_input = get_file("data.year2015", "day06-input.txt").readlines()
        result = solve_puzzle_2(puzzle_input)

        assert result["answer"] == 14687245