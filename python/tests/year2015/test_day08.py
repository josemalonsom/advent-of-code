from tests.helper import get_file
from year2015.day08 import solve_puzzle_1, solve_puzzle_2


class TestDay07:

    def test_examples_puzzle_1(self):

        puzzle_input = [
            r'""',
            r'"abc"',
            r'"aaa\"aaa"',
            r'"\x27"'
        ]

        assert solve_puzzle_1(puzzle_input) == 12

    def test_puzzle_1(self):
        lines = get_file("data.year2015", "day08-input.txt").readlines()
        puzzle_input = [line.strip('\n') for line in lines]

        assert solve_puzzle_1(puzzle_input) == 1371

    def test_examples_puzzle_2(self):

        puzzle_input = [
            r'""',
            r'"abc"',
            r'"aaa\"aaa"',
            r'"\x27"'
        ]

        assert solve_puzzle_2(puzzle_input) == 19

    def test_puzzle_2(self):
        lines = get_file("data.year2015", "day08-input.txt").readlines()
        puzzle_input = [line.strip('\n') for line in lines]

        assert solve_puzzle_2(puzzle_input) == 2117
