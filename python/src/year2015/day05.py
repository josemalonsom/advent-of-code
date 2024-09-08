#!/usr/bin/env python3

# https://adventofcode.com/2015/day/5

import re


def solve_puzzle_1(puzzle_input):

    number_of_nice_strings = 0

    for string in puzzle_input:
        if re.match(".*(ab|cd|pq|xy).*", string):
            continue

        matches_nice_conditions = \
            re.match(".*[aeiou].*[aeiou].*[aeiou].*", string) \
            and re.match(".*([a-z])\\1.*", string)

        if matches_nice_conditions:
            number_of_nice_strings += 1

    return {
        "answer": number_of_nice_strings
    }


def solve_puzzle_2(puzzle_input):

    number_of_nice_strings = 0

    for string in puzzle_input:
        # if re.match(".*([a-z])([a-z])\\2.*", string):
        #     continue

        matches_nice_conditions = \
            re.match(".*(([a-z])([a-z])(?!\\3))(.*)\\1.*", string) \
            and re.match(".*([a-z]).\\1.*", string)

        if matches_nice_conditions:
            number_of_nice_strings += 1

    return {
        "answer": number_of_nice_strings
    }
