bad_strings = ["ab", "cd", "pq", "xy"]


def is_nice_part_1(string: str):
    vowel_counter = 0
    double_letter = False
    bad_string = False

    for i in range(len(string) - 1):
        vowel_counter = (
            string.count("a")
            + string.count("e")
            + string.count("i")
            + string.count("o")
            + string.count("u")
        )
        if string[i] == string[i + 1]:
            double_letter = True
        if string[i : i + 2] in bad_strings:
            bad_string = True

    return vowel_counter >= 3 and double_letter and not bad_string


def is_nice_part_2(string: str):
    double_double = False
    sandwich = False

    for i in range(0, (len(string) - 2)):
        if double_double == True:
            break
        substring = string[i : i + 2]
        for j in range(i + 2, len(string)):
            if string[j : j + 2] == substring:
                double_double = True
                break

    for i in range(len(string) - 2):
        if sandwich == True:
            break
        if string[i] == string[i + 2]:
            sandwich = True

    return double_double and sandwich


def determine_nice_strings(pt: int):
    with open("input.txt", "r") as f:
        strings = f.read().splitlines()

    total_nice = 0
    for string in strings:
        if pt == 1:
            total_nice += 1 if is_nice_part_1(string) else 0
        else:
            total_nice += 1 if is_nice_part_2(string) else 0

    return total_nice


if __name__ == "__main__":
    print(f"Solution 1: {determine_nice_strings(1)} nice strings")
    print(f"Solution 2: {determine_nice_strings(2)} nice strings")
