from tests.helper import get_file
from year2015.day07 import solve_puzzle_1, solve_puzzle_2


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

        assert solve_puzzle_1(puzzle_input, "d") == 72
        assert solve_puzzle_1(puzzle_input, "e") == 507
        assert solve_puzzle_1(puzzle_input, "f") == 492
        assert solve_puzzle_1(puzzle_input, "g") == 114
        assert solve_puzzle_1(puzzle_input, "h") == 65412
        assert solve_puzzle_1(puzzle_input, "i") == 65079
        assert solve_puzzle_1(puzzle_input, "x") == 123
        assert solve_puzzle_1(puzzle_input, "y") == 456

    def test_signal_with_and(self):

        puzzle_input = [
            "123 -> x",
            "1 AND x -> d"
        ]

        assert solve_puzzle_1(puzzle_input, "x") == 123
        assert solve_puzzle_1(puzzle_input, "d") == 1

    def test_pass_one_wire_value_to_another(self):

        puzzle_input = [
            "123 -> x",
            "x -> d"
        ]

        assert solve_puzzle_1(puzzle_input, "d") == 123

    def test_puzzle_1(self):
        puzzle_input = get_file("data.year2015", "day07-input.txt").readlines()

        assert solve_puzzle_1(puzzle_input, "a") == 16076

    def test_puzzle_2(self):
        puzzle_input = get_file("data.year2015", "day07-input.txt").readlines()

        assert solve_puzzle_2(puzzle_input, "a") == 2797
