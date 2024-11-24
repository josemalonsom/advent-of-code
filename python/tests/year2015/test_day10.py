import pytest

from year2015.day10 import compute_input, compute_input_times


class TestDay10:

    @pytest.mark.parametrize("puzzle_input, expected_result", [
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("1211", "111221"),
        ("111221", "312211")
    ])
    def test_examples_puzzle_1(self, puzzle_input, expected_result):
        assert compute_input_times(puzzle_input, 1) == expected_result

    def test_puzzle_1(self):
        assert len(compute_input_times("1113122113", 40)) == 360154

    def test_puzzle_2(self):
        assert len(compute_input_times("1113122113", 50)) == 5103798
