import os
import time


def parse_input():
    s = open("input.txt").read().strip()
    s = s.split("\n")

    walls = set()
    max_y = 0
    for wall in s:
        wall = wall.split(" -> ")
        for i in range(1, len(wall)):
            x, y = wall[i].split(",")
            x = int(x)
            y = int(y)
            prev_x, prev_y = wall[i - 1].split(",")
            prev_x = int(prev_x)
            prev_y = int(prev_y)
            if y > max_y or prev_y > max_y:
                max_y = max(y, prev_y)
            if x == prev_x:
                for ty in range(min(y, prev_y), max(y, prev_y) + 1):
                    walls.add((x, ty))
            else:
                for tx in range(min(x, prev_x), max(x, prev_x) + 1):
                    walls.add((tx, y))
    max_y += 2

    return walls, max_y


def generate_scan(rocks, x_range, y_max):
    scan = [[" " for _ in range(x_range[1] + 1)] for _ in range(y_max)]
    for y in range(y_max):
        for x in range(x_range[1] + 1):
            if (x + x_range[0], y) in rocks:
                scan[y][x] = "#"
            else:
                scan[y][x] = "."
    return scan


def print_scan(rocks, sand, y_max):
    min_x = float("inf")
    max_x = 0
    for x, y in rocks:
        min_x = x if x < min_x else min_x
        max_x = x if x > max_x else max_x
    for x, y in sand:
        min_x = x if x < min_x else min_x
        max_x = x if x > max_x else max_x

    x_range = max_x - min_x

    for y in range(y_max):
        row_string = ""
        for x in range(x_range):
            if (x + min_x, y) in rocks:
                row_string += "#"
            elif (x + min_x, y) in sand:
                row_string += "o"
            else:
                row_string += "."

        print(f"{str(y+1).zfill(3)}: {row_string}")


def predict_sand_fall(rocks, y_max, pt=1):
    total_sand = 0
    sand = set()

    while True:
        if pt == 2 and (500, 0) in sand:
            return len(sand)

        x = 500
        y = 0

        while True:
            if y + 1 == y_max:
                if pt == 1:
                    return len(sand)
                else:
                    sand.add((x, y))
                    break
            if (x, y + 1) not in rocks and (x, y + 1) not in sand:
                y += 1
                continue
            elif (x - 1, y + 1) not in rocks and (x - 1, y + 1) not in sand:
                y += 1
                x -= 1
                continue
            elif (x + 1, y + 1) not in rocks and (x + 1, y + 1) not in sand:
                y += 1
                x += 1
                continue
            sand.add((x, y))
            total_sand += 1
            break


if __name__ == "__main__":
    start_time = time.time()
    x_range = [410, 98]

    rocks, y_max = parse_input()
    scan = generate_scan(rocks, x_range, y_max)
    pt_1 = predict_sand_fall(rocks, y_max)
    pt_2 = predict_sand_fall(rocks, y_max, pt=2)
    print(f"Solution 1: {pt_1} total units of sand")
    print(f"Solution 2: {pt_2} total units of sand")
    print(f"Total elapsed time: {time.time()-start_time} seconds")
