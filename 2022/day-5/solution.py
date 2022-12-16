with open("input.txt", "r") as f:
    lines = f.readlines()

with open("input2.txt", "r") as f:
    moves = f.readlines()

stacks = [
    list(lines[0].replace("\n", "").split(",")),
    list(lines[1].replace("\n", "").split(",")),
    list(lines[2].replace("\n", "").split(",")),
    list(lines[3].replace("\n", "").split(",")),
    list(lines[4].replace("\n", "").split(",")),
    list(lines[5].replace("\n", "").split(",")),
    list(lines[6].replace("\n", "").split(",")),
    list(lines[7].replace("\n", "").split(",")),
    list(lines[8].replace("\n", "").split(",")),
]


def move_boxes():
    for stack in stacks:
        print(stack)
    for move in moves:
        print("")
        move = move.replace("\n", "").split(" ")
        number_of_boxes = int(move[1])
        start_stack = int(move[3]) - 1
        end_stack = int(move[5]) - 1

        pickup = stacks[start_stack][0:number_of_boxes]
        del stacks[start_stack][0:number_of_boxes]
        pickup.extend(stacks[end_stack])
        stacks[end_stack] = pickup

        for stack in stacks:
            print(stack)

    final = ""
    for stack in stacks:
        if stack:
            final += stack[0]

    print(final)


move_boxes()
