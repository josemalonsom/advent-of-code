#!/usr/bin/env python3

# https://adventofcode.com/2015/day/7

operations_by_wire = {}
values_by_wire = {}


def solve_puzzle_1(puzzle_input, wire):

    operations_by_wire.clear()
    values_by_wire.clear()

    for instruction in puzzle_input:
        operation, output_wire = [item.strip() for item in instruction.split("->")]
        operations_by_wire[output_wire] = [item.strip() for item in operation.split()]

    return get_wire_output(wire)


def get_wire_output(wire):

    if wire in values_by_wire:
        return values_by_wire[wire]

    operation = operations_by_wire[wire]

    match len(operation):
        case 2:
            operator = operation[0]
        case 3:
            operator = operation[1]
        case _:
            operator = "SIGNAL"

    match operator:
        case "SIGNAL":
            isnumeric = operation[0].isnumeric()
            output = operation[0] if isnumeric else get_wire_output(operation[0])
        case "AND":
            left_value = int(operation[0]) if operation[0].isnumeric() else get_wire_output(operation[0])
            output = left_value & get_wire_output(operation[2])
        case "LSHIFT":
            output = get_wire_output(operation[0]) << int(operation[2])
        case "RSHIFT":
            output = get_wire_output(operation[0]) >> int(operation[2])
        case "OR":
            output = get_wire_output(operation[0]) | get_wire_output(operation[2])
        case "NOT":
            output = 65536 + (~ get_wire_output(operation[1]))
        case _:
            raise Exception(f"Operation not identified: {operation} wire: {wire}")

    values_by_wire[wire] = int(output)

    return values_by_wire[wire]


def solve_puzzle_2(puzzle_input, wire):

    operations_by_wire.clear()
    values_by_wire.clear()
    values_by_wire["b"] = 16076

    for instruction in puzzle_input:
        operation, output_wire = [item.strip() for item in instruction.split("->")]
        operations_by_wire[output_wire] = [item.strip() for item in operation.split()]

    return get_wire_output(wire)
