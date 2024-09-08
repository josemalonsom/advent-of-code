#!/usr/bin/env python3

# https://adventofcode.com/2015/day/6

import re
from enum import Enum

class Action(Enum):
    TURN_ON = 1,
    TURN_OFF = 2
    TOGGLE = 3

def solve_puzzle_1(puzzle_input):

    num_rows, num_columns = 1_000, 1_000

    grid = [[False] * num_columns for _ in range(num_rows)]
    pattern = re.compile(".*?([0-9]+),([0-9]+).*?([0-9]+),([0-9]+).*?")

    for instruction in puzzle_input:
        if str(instruction).startswith("toggle"):
            action = Action.TOGGLE
        elif str(instruction).startswith("turn on"):
            action = Action.TURN_ON
        else:
            action = Action.TURN_OFF

        match_result = pattern.match(instruction)
        start_coordinates = (int(match_result.group(1)), int(match_result.group(2)))
        end_coordinates = (int(match_result.group(3)), int(match_result.group(4)))

        for x in range(start_coordinates[0], end_coordinates[0] + 1):
            for y in range(start_coordinates[1], end_coordinates[1] + 1):
                match action:
                    case Action.TOGGLE:
                        grid[x][y] = not grid[x][y]
                    case Action.TURN_ON:
                        grid[x][y] = True
                    case Action.TURN_OFF:
                        grid[x][y] = False

    total_lights_lit = 0
    for x in range(0, num_columns):
        for y in range(0, num_rows):
            if grid[x][y]:
                total_lights_lit += 1

    return {
        "answer": total_lights_lit
    }

def solve_puzzle_2(puzzle_input):

    num_rows, num_columns = 1_000, 1_000

    grid = [[0] * num_columns for _ in range(num_rows)]
    pattern = re.compile(".*?([0-9]+),([0-9]+).*?([0-9]+),([0-9]+).*?")

    for instruction in puzzle_input:
        if str(instruction).startswith("toggle"):
            action = Action.TOGGLE
        elif str(instruction).startswith("turn on"):
            action = Action.TURN_ON
        else:
            action = Action.TURN_OFF

        match_result = pattern.match(instruction)
        start_coordinates = (int(match_result.group(1)), int(match_result.group(2)))
        end_coordinates = (int(match_result.group(3)), int(match_result.group(4)))

        for x in range(start_coordinates[0], end_coordinates[0] + 1):
            for y in range(start_coordinates[1], end_coordinates[1] + 1):
                match action:
                    case Action.TOGGLE:
                        grid[x][y] += 2
                    case Action.TURN_ON:
                        grid[x][y] += 1
                    case Action.TURN_OFF:
                        grid[x][y] = 0 if grid[x][y] - 1 < 0 else grid[x][y] - 1

    total_brightness = 0
    for x in range(0, num_columns):
        for y in range(0, num_rows):
            total_brightness += grid[x][y]

    return {
        "answer": total_brightness
    }
