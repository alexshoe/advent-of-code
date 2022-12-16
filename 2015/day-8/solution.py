def parse_text():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    literal_length = 0
    memory_length = 0
    new_length = 0

    for line in lines:
        literal_length += len(line)

        x = eval(line)
        memory_length += len(x)

        new_length += len(line) + 2
        for char in line:
            if char in ["\\", '"']:
                new_length += 1

    return (literal_length - memory_length), (new_length - literal_length)


if __name__ == "__main__":
    pt_one, pt_two = parse_text()
    print(f"Solution 1: Difference between literal and in-memory length is:{pt_one}")
    print(f"Solution 2: Difference between encoded and literal length is:{pt_two}")
