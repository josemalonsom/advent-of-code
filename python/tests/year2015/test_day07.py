from tests.helper import get_file
from year2015.day07 import solve_puzzle_1


class TestDay07:

    def test_examples_puzzle_1(self):

        puzzle_input = [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i"
        ]

        result = solve_puzzle_1(puzzle_input)

        assert result == {
            "d": 72,
            "e": 507,
            "f": 492,
            "g": 114,
            "h": 65412,
            "i": 65079,
            "x": 123,
            "y": 456
        }

    def test_signal_with_and(self):

        puzzle_input = [
            "123 -> x",
            "1 AND x -> d"
        ]

        result = solve_puzzle_1(puzzle_input)

        assert result == {
            "x": 123,
            "d": 1
        }

    def test_puzzle_1(self):
        puzzle_input = get_file("data.year2015", "day07-input.txt").readlines()
        result = solve_puzzle_1(puzzle_input)

        assert result["a"] == 0
