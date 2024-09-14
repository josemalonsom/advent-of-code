import codecs


# https://adventofcode.com/2015/day/8

def solve_puzzle_1(puzzle_input):

    number_of_code_characters = 0
    number_of_characters_in_memory = 0

    for string in puzzle_input:
        number_of_code_characters += len(string)

        number_of_characters_in_memory += len(codecs.decode(string, 'unicode_escape'))

        # subtract the double quotes around the string
        number_of_characters_in_memory -= 2

    return number_of_code_characters - number_of_characters_in_memory


def solve_puzzle_2(puzzle_input):

    number_of_code_characters = 0
    number_of_encoded_characters = 0

    for string in puzzle_input:
        number_of_code_characters += len(string)

        string = string.replace('\\', '\\\\').replace('"', '\\"')
        number_of_encoded_characters += len(string)

        # add the double quotes around the string
        number_of_encoded_characters += 2

    return number_of_encoded_characters - number_of_code_characters
