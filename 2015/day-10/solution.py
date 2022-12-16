from itertools import groupby


def look_and_say(number, n):
    for i in range(n):
        new_string = ""
        num_groups = groupby(number)
        result = [(label, sum(1 for _ in group)) for label, group in num_groups]
        for digit in result:
            new_string += str(digit[1]) + digit[0]
        number = new_string

    return number


if __name__ == "__main__":
    final_input = "1321131112"
    answer = look_and_say(final_input, 50)
    print(f"Solution 1: {len(answer)}")
