from dataclasses import dataclass
from itertools import combinations, permutations


@dataclass
class City:
    name: str
    neighbors: dict


def parse_data():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    cities = {}
    for line in lines:
        line = line.split(" = ")
        city_a = line[0].split(" to ")[0]
        city_b = line[0].split(" to ")[1]
        distance = line[1]

        if city_a in cities.keys():
            cities[city_a].neighbors[city_b] = distance
        else:
            cities[city_a] = City(name=city_a, neighbors={city_b: distance})

        if city_b in cities.keys():
            cities[city_b].neighbors[city_a] = distance
        else:
            cities[city_b] = City(name=city_b, neighbors={city_a: distance})

    return cities


def get_combinations(cities: dict):
    sample_list = list(cities.keys())
    list_combinations = list()
    list_combinations += list(permutations(sample_list, len(cities)))
    return list_combinations


def find_distances(cities, combos):
    shortest_path = float("inf")
    longest_path = 0
    for combo in combos:
        distance = 0
        for i in range(len(combo) - 1):
            distance += int(cities[combo[i]].neighbors[combo[i + 1]])
        shortest_path = distance if distance < shortest_path else shortest_path
        longest_path = distance if distance > longest_path else longest_path

    return shortest_path, longest_path


if __name__ == "__main__":
    cities = parse_data()
    combos = get_combinations(cities)
    shortest, longest = find_distances(cities, combos)
    print(f"Solution 1: The shortest path is {shortest} long")
    print(f"Solution 2: The longest path is {longest} long")
