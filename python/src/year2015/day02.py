#!/usr/bin/env python3

# https://adventofcode.com/2015/day/2

def solve(dimensions_boxes):

    total_square_feet_of_wrapping_paper = 0
    total_ribbon_length = 0

    for dimensions in dimensions_boxes:
        (length, width, height) = [int(x) for x in dimensions.split("x")]

        # Ribbon calculation
        values = [length, width, height]
        values.sort()
        smallest_side_perimeter = values[0] + values[0] + values[1] + values[1]
        volume = length * width * height

        total_ribbon_length += smallest_side_perimeter + volume

        # Wrapping paper calculation
        area_side_1 = length * width
        area_side_2 = width * height
        area_side_3 = height * length

        all_areas = [area_side_1, area_side_2, area_side_3]
        smallest_area = min(all_areas)

        areas_all_sides = [area * 2 for area in all_areas]
        square_feet_of_wrapping_paper = areas_all_sides[0] + areas_all_sides[1] + areas_all_sides[2] + smallest_area

        total_square_feet_of_wrapping_paper += square_feet_of_wrapping_paper

    return {
        "total_square_feet_of_wrapping_paper": total_square_feet_of_wrapping_paper,
        "total_ribbon_length": total_ribbon_length
    }
