def total_houses_delivered(with_robo_santa=False):
    with open("input.txt") as f:
        moves = f.read()

    x_coord = y_coord = x_coord_robo = y_coord_robo = 0

    santas_turn = True
    visited = set()
    visited.add((x_coord, y_coord))

    for move in moves:
        if santas_turn:
            if move == "^":
                y_coord += 1
                print(f"{move}: Moving to the North")
            elif move == "v":
                y_coord -= 1
                print(f"{move}: Moving to the South")
            elif move == ">":
                x_coord += 1
                print(f"{move}: Moving to the East")
            else:
                x_coord -= 1
                print(f"{move}: Moving to the West`")
            print(f"Santa's new coordinates are ({x_coord}, {y_coord})")
            visited.add((x_coord, y_coord))
            santas_turn = False if with_robo_santa else True
        else:
            if move == "^":
                y_coord_robo += 1
                print(f"{move}: Robo moving to the North")
            elif move == "v":
                y_coord_robo -= 1
                print(f"{move}: Robo moving to the South")
            elif move == ">":
                x_coord_robo += 1
                print(f"{move}: Robo moving to the East")
            else:
                x_coord_robo -= 1
                print(f"{move}: Robo moving to the West`")
            print(f"Robo's new coordinates are ({x_coord_robo}, {y_coord_robo})")
            visited.add((x_coord_robo, y_coord_robo))
            santas_turn = True

    print("")
    return len(visited)


if __name__ == "__main__":
    houses_visited = total_houses_delivered()
    houses_visited_robo = total_houses_delivered(with_robo_santa=True)
    print(f"Solution 1: {houses_visited} houses visited")
    print(f"Solution 2: {houses_visited_robo} houses visited")
