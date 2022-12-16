with open("input.txt", "r") as f:
    buffer = f.readlines()[0]


def has_unique_chars(string: str, length: int):
    unique_chars = "".join(set(string))
    return len(unique_chars) == length


def length_before_marker():
    for i in range(0, len(buffer) - 4):
        four_string = buffer[i : i + 4]
        if has_unique_chars(four_string, 4):
            return i + 4

    return "No start-of-packet marker found"


def length_before_message():
    for i in range(0, len(buffer) - 14):
        fourteen_string = buffer[i : i + 14]
        if has_unique_chars(fourteen_string, 14):
            return i + 14

    return "No start-of-message marker found"


if __name__ == "__main__":
    print(f"Solution 1: {length_before_marker()}")
    print(f"Solution 2: {length_before_message()}")
