import pytest

from tests.helper import get_file
from year2015.day05 import solve_puzzle_1, solve_puzzle_2


class TestDay03:

    @pytest.mark.parametrize("puzzle_input, expected_number_of_nice_strings", [
        (["ugknbfddgicrmopn"], 1),
        (["aaa"], 1),
        (["jchzalrnumimnmhp"], 0),
        (["haegwjzuvuyypxyu"], 0),
        (["dvszwmarrgswjxmb"], 0),
        (["ugknbfddgicrmopn", "dvszwmarrgswjxmb"], 1),
        (["ugknbfddgicrmopn", "dvszwmarrgswjxmb",  "aaa"], 2),
        (["ab", "cd", "pq", "xy", "aaba", "acda", "apqa", "axya"], 0),
        (["def"], 0),
        (["aeiouu"], 1)
    ])
    def test_examples_puzzle_1(self, puzzle_input, expected_number_of_nice_strings):
        result = solve_puzzle_1(puzzle_input)

        assert result["answer"] == expected_number_of_nice_strings

    def test_puzzle_1(self):
        puzzle_input = get_file("data.year2015", "day05-input.txt").readlines()
        result = solve_puzzle_1(puzzle_input)

        assert result["answer"] == 258

    @pytest.mark.parametrize("puzzle_input, expected_number_of_nice_strings", [
        (["qjhvhtzxzqqjkmpb"], 1),
        (["xxyxx"], 1),
        (["uurcxstgmygtbstg"], 0),
        (["ieodomkazucvgmuy"], 0)
    ])
    def test_examples_puzzle_2(self, puzzle_input, expected_number_of_nice_strings):
        result = solve_puzzle_2(puzzle_input)

        assert result["answer"] == expected_number_of_nice_strings

    def test_puzzle_2(self):
        puzzle_input = get_file("data.year2015", "day05-input.txt").readlines()
        result = solve_puzzle_2(puzzle_input)

        assert result["answer"] == 53
