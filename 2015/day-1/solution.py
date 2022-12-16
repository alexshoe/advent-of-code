def calculate_moves():
    with open("input.txt") as f:
        moves = f.read()

    floor = 0
    first_basement = None
    found = False
    for i in range(len(moves)):
        floor += 1 if moves[i] == "(" else -1
        if floor == -1 and found == False:
            first_basement = i + 1
            found = True

    return floor, first_basement


if __name__ == "__main__":
    final_floor, first_basement_position = calculate_moves()
    print(f"Part 1: Santa finished on floor {final_floor}")
    print(
        f"Part 2: The position of the first basement move is {first_basement_position}"
    )
