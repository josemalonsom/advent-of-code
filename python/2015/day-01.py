#!/usr/bin/env python3

# https://adventofcode.com/2015/day/1

UP = "("
input_file = open("day-01-input.txt", "r")
puzzle_input = input_file.read()

inputArray = ([*puzzle_input])
currentFloor = 0
indexFirstCharacterThatCausesEnteringBasement = None

for idx, character in enumerate(inputArray):
    currentFloor += 1 if character == UP else -1

    if indexFirstCharacterThatCausesEnteringBasement is None and currentFloor == -1:
        indexFirstCharacterThatCausesEnteringBasement = idx + 1

print('Current Floor: ' + str(currentFloor))
print("Index First Character That Causes Entering Basement: " + str(indexFirstCharacterThatCausesEnteringBasement))

