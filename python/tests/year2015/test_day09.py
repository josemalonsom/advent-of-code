from tests.helper import get_file
from year2015.day09 import solve_puzzle_1, solve_puzzle_2


class TestDay09:

    def test_examples_puzzle_1(self):

        puzzle_input = [
            "London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141"
        ]

        assert solve_puzzle_1(puzzle_input) == 605

    def test_puzzle_1(self):
        puzzle_input = get_file("data.year2015", "day09-input.txt").readlines()

        assert solve_puzzle_1(puzzle_input) == 207

    def test_examples_puzzle_2(self):

        puzzle_input = [
            "London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141"
        ]

        assert solve_puzzle_2(puzzle_input) == 982

    def test_puzzle_2(self):
        puzzle_input = get_file("data.year2015", "day09-input.txt").readlines()

        assert solve_puzzle_2(puzzle_input) == 804
