#!/usr/bin/env python3

# https://adventofcode.com/2015/day/6

import re
from enum import Enum

COORDINATES_PATTERN = re.compile(".*?([0-9]+),([0-9]+).*?([0-9]+),([0-9]+).*?")
NUM_COLUMNS = 1_000
NUM_ROWS = 1_000


class Action(Enum):
    TURN_ON = 1,
    TURN_OFF = 2
    TOGGLE = 3

    @staticmethod
    def get_action_for_instruction(instruction):
        if str(instruction).startswith("toggle"):
            return Action.TOGGLE
        elif str(instruction).startswith("turn on"):
            return Action.TURN_ON
        else:
            return Action.TURN_OFF


def solve_puzzle_1(puzzle_input):

    grid = initialize_grid()

    for instruction in puzzle_input:
        action = Action.get_action_for_instruction(instruction)
        end_coordinates, start_coordinates = get_coordinates(instruction)

        for x in range(start_coordinates[0], end_coordinates[0] + 1):
            for y in range(start_coordinates[1], end_coordinates[1] + 1):
                match action:
                    case Action.TOGGLE:
                        grid[x][y] = 0 if grid[x][y] else 1
                    case Action.TURN_ON:
                        grid[x][y] = 1
                    case Action.TURN_OFF:
                        grid[x][y] = 0

    return {
        "answer": get_total(grid)
    }


def initialize_grid():
    return [[0] * NUM_COLUMNS for _ in range(NUM_ROWS)]


def get_coordinates(instruction):
    match_result = COORDINATES_PATTERN.match(instruction)
    start_coordinates = (int(match_result.group(1)), int(match_result.group(2)))
    end_coordinates = (int(match_result.group(3)), int(match_result.group(4)))

    return end_coordinates, start_coordinates


def get_total(grid):
    total = 0
    for x in range(0, NUM_COLUMNS):
        for y in range(0, NUM_ROWS):
            total += grid[x][y]
    return total


def solve_puzzle_2(puzzle_input):

    grid = initialize_grid()

    for instruction in puzzle_input:
        action = Action.get_action_for_instruction(instruction)
        end_coordinates, start_coordinates = get_coordinates(instruction)

        for x in range(start_coordinates[0], end_coordinates[0] + 1):
            for y in range(start_coordinates[1], end_coordinates[1] + 1):
                match action:
                    case Action.TOGGLE:
                        grid[x][y] += 2
                    case Action.TURN_ON:
                        grid[x][y] += 1
                    case Action.TURN_OFF:
                        grid[x][y] = 0 if grid[x][y] - 1 < 0 else grid[x][y] - 1

    return {
        "answer": get_total(grid)
    }
