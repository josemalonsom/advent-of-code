#!/usr/bin/env python3

# https://adventofcode.com/2015/day/3

class Movements:
    NORTH = "^"
    SOUTH = "v"
    EAST = ">"
    WEST = "<"


def solve_puzzle_1(puzzle_input):
    moves = ([*puzzle_input])
    current_coordinates = {"x": 0, "y": 0}
    coordinates_visited = {(0, 0)}

    for move in moves:
        update_coordinates(current_coordinates, move, coordinates_visited)

    return {
        "total_houses_receiving_presents": len(coordinates_visited)
    }


def update_coordinates(current_coordinates, move, coordinates_visited):

    match move:
        case Movements.NORTH:
            current_coordinates["y"] += 1
        case Movements.SOUTH:
            current_coordinates["y"] -= 1
        case Movements.EAST:
            current_coordinates["x"] += 1
        case _:
            current_coordinates["x"] -= 1

    coordinates_visited.add((current_coordinates["x"], current_coordinates["y"]))


def solve_puzzle_2(puzzle_input):
    moves = ([*puzzle_input])

    santa_coordinates = {"x": 0, "y": 0}
    robo_santa_coordinates = {"x": 0, "y": 0}
    is_santa_turn = True
    coordinates_visited = {(0, 0)}

    for move in moves:
        current_coordinates = santa_coordinates if is_santa_turn else robo_santa_coordinates
        update_coordinates(current_coordinates, move, coordinates_visited)

        is_santa_turn = not is_santa_turn

    return {
        "total_houses_receiving_presents": len(coordinates_visited)
    }
