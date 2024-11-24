# https://adventofcode.com/2015/day/10
import re


def compute_input_times(puzzle_input, times):
    accumulated_input = puzzle_input

    for i in range(times):
        accumulated_input = compute_input(accumulated_input)

    return accumulated_input


def compute_input(puzzle_input):
    result = ""
    pattern = re.compile(r"([0-9])\1*")

    for match in pattern.finditer(puzzle_input):
        result += str(len(match.group())) + match.group()[0]

    return result
