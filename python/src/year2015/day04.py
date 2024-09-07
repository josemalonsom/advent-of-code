#!/usr/bin/env python3

# https://adventofcode.com/2015/day/4

import hashlib


def solve_puzzle(puzzle_input, number_of_zeroes=5):

    number = 0
    prefix = "".zfill(number_of_zeroes)

    while True:
        md5input = puzzle_input + str(number)
        md5hash = hashlib.md5(md5input.encode()).hexdigest()

        if md5hash.startswith(prefix):
            break

        number += 1

    return {
        "answer": number
    }
