#!/usr/bin/env python3
import re

# https://adventofcode.com/2015/day/7


def solve_puzzle_1(puzzle_input):

    pattern = re.compile("(.*) -> (.*)")
    operations_by_wire = {}

    for instruction in puzzle_input:

        match = pattern.match(instruction)
        operation = match.group(1)
        wire = match.group(2)

        operations_by_wire[wire] = operation

    output_by_wire = {}

    for wire in operations_by_wire:

        output_by_wire[wire] = get_wire_output(wire, operations_by_wire, output_by_wire)

    return output_by_wire


def get_wire_output(wire, operations_by_wire, output_by_wire):

    operation = operations_by_wire[wire]

    # send signal to wire: 123 -> x
    if re.match("[0-9]+(?!.*[A-Z].*)", operation):
        return int(operation)

    # [0-9] AND y -> d
    match = re.match("([0-9]+) AND (.*)", operation)
    if match:
        signal = int(match.group(1))
        wire2 = match.group(2)

        if wire2 not in output_by_wire:
            output_by_wire[wire2] = get_wire_output(wire2, operations_by_wire, output_by_wire)

        return signal & output_by_wire[wire2]

    # x AND y -> d
    match = re.match("(.*) AND (.*)", operation)
    if match:
        wire1 = match.group(1)
        wire2 = match.group(2)

        if wire1 not in output_by_wire:
            output_by_wire[wire1] = get_wire_output(wire1, operations_by_wire, output_by_wire)
        if wire2 not in output_by_wire:
            output_by_wire[wire2] = get_wire_output(wire2, operations_by_wire, output_by_wire)

        return output_by_wire[wire1] & output_by_wire[wire2]

    # x OR y -> e
    match = re.match("(.*) OR (.*)", operation)
    if match:
        wire1 = match.group(1)
        wire2 = match.group(2)

        if wire1 not in output_by_wire:
            output_by_wire[wire1] = get_wire_output(wire1, operations_by_wire, output_by_wire)
        if wire2 not in output_by_wire:
            output_by_wire[wire2] = get_wire_output(wire2, operations_by_wire, output_by_wire)

        return output_by_wire[wire1] | output_by_wire[wire2]

    # p LSHIFT 2 -> q
    match = re.match("(.*) LSHIFT (.*)", operation)
    if match:
        wire1 = match.group(1)
        positions = int(match.group(2))

        if wire1 not in output_by_wire:
            output_by_wire[wire1] = get_wire_output(wire1, operations_by_wire, output_by_wire)

        return output_by_wire[wire1] << positions

    # y RSHIFT 2 -> g
    match = re.match("(.*) RSHIFT (.*)", operation)
    if match:
        wire1 = match.group(1)
        positions = int(match.group(2))

        if wire1 not in output_by_wire:
            output_by_wire[wire1] = get_wire_output(wire1, operations_by_wire, output_by_wire)

        return output_by_wire[wire1] >> positions

    # NOT x -> h
    match = re.match("NOT (.*)", operation)
    if match:
        wire1 = match.group(1)

        if wire1 not in output_by_wire:
            output_by_wire[wire1] = get_wire_output(wire1, operations_by_wire, output_by_wire)

        return 65536 + (~ output_by_wire[wire1])
