# https://adventofcode.com/2015/day/9
import re
from itertools import permutations


def solve_puzzle_1(distances):
    return get_routes_distances(distances)[0]


def solve_puzzle_2(distances):
    return get_routes_distances(distances)[-1]


def get_routes_distances(distances):

    pattern = re.compile("([a-zA-Z]+) to ([a-zA-Z]+) = ([0-9]+)")
    cities = []
    distances_between_cities = {}

    for distance in distances:
        distance_values = pattern.match(distance).groups()
        cities.extend(distance_values[0:2])
        distances_between_cities[(distance_values[0]), distance_values[1]] = int(distance_values[2])
        distances_between_cities[(distance_values[1]), distance_values[0]] = int(distance_values[2])

    unique_cities = set(cities)
    possible_routes = list(permutations(unique_cities))
    routes_distances = []

    for route in possible_routes:
        route_distance = 0
        city_from = route[0]
        for city in route[1:]:
            city_to = city
            route_distance += distances_between_cities[(city_from, city_to)]
            city_from = city_to
        routes_distances.append(route_distance)

    routes_distances.sort()
    return routes_distances
