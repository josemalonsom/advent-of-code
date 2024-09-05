#!/usr/bin/env python3

# https://adventofcode.com/2015/day/1

UP = "("
# input_file = open("day-01-input.txt", "r")
# puzzle_input = input_file.read()

def solve(puzzle_input):
    input_array = ([*puzzle_input])
    current_floor = 0
    index_first_character_that_causes_entering_basement = None

    for idx, character in enumerate(input_array):
        current_floor += 1 if character == UP else -1

        if index_first_character_that_causes_entering_basement is None and current_floor == -1:
            index_first_character_that_causes_entering_basement = idx + 1

    return {
        "current_floor": current_floor,
        "position_character_taking_to_basement": index_first_character_that_causes_entering_basement
    }