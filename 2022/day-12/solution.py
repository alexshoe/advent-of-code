import time
from dataclasses import dataclass
from collections import deque


@dataclass
class Hill:
    height: str
    adjacent: list[tuple[int, int]]
    visited: bool
    parent: tuple[int, int]
    distance: float
    coordinates: tuple[int, int]


def parse_input():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    return lines


def get_start_and_end(data):
    new_data = []
    for y, line in enumerate(data):
        new_line = ""
        for x, char in enumerate(line):
            if char == "S":
                start = (x, y)
                char = "a"

            if char == "E":
                end = (x, y)
                char = "z"

            new_line += char
        new_data.append(new_line)

    return start, end, new_data


def get_hill_grid(data):
    grid = []

    for y, line in enumerate(data):
        row = []

        for x, char in enumerate(line):
            height = char
            adjacent = []
            visited = False
            parent = None
            distance = float("inf")
            coordinates = (x, y)
            # Look for adjecent hill to left
            if x != 0 and ord(data[y][x - 1]) <= ord(char) + 1:
                adjacent.append((x - 1, y))
            # Look for adjecent hill to right
            if x != (len(line) - 1) and ord(data[y][x + 1]) <= ord(char) + 1:
                adjacent.append((x + 1, y))
            # Look for adjecent hill above
            if y != 0 and ord(data[y - 1][x]) <= ord(char) + 1:
                adjacent.append((x, y - 1))
            # Look for adjecent hill below
            if y != (len(data) - 1) and ord(data[y + 1][x]) <= ord(char) + 1:
                adjacent.append((x, y + 1))
            row.append(Hill(height, adjacent, visited, parent, distance, coordinates))

        grid.append(row)

    return grid


def breadth_first_search(
    grid: list[list[Hill]], start: tuple[int, int], end: tuple[int, int]
):
    queue = deque([(0, start)])
    print(grid)
    grid[start[1]][start[0]].visited = True

    while queue:
        num_steps, current_pos = queue.popleft()
        print(f"Now at: ({current_pos})")
        x, y = current_pos
        if current_pos == end:
            print("Found the highest point!")
            return num_steps
        for n in grid[y][x].adjacent:
            print(f"{current_pos}'s Neighbors: {grid[y][x].adjacent}")
            n_x, n_y = n
            if not grid[n_y][n_x].visited:
                print("")
                print(f"Going from {current_pos} to {n}")
                grid[n_y][n_x].visited = True
                queue.append((num_steps + 1, n))
                print(f"Queue: {queue}")

    return float("inf")


if __name__ == "__main__":
    start_time = time.time()
    data = parse_input()
    start, end, data = get_start_and_end(data)
    grid = get_hill_grid(data)
    bfs_path = breadth_first_search(grid, start, end)
