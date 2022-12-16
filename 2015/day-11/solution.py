def check_password(password):
    def increasing_straight(password):
        for i in range(len(password) - 2):
            if ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2:
                return True
        return False

    def forbidden_chars(password):
        for i in range(len(password)):
            if password[i] in ["i", "o", "l"]:
                return False
        return True

    def non_overlapping_doubles(password):
        for i in range(len(password) - 3):
            if password[i] == password[i + 1]:
                for j in range(i + 2, len(password) - 1):
                    if password[j] == password[j + 1]:
                        return True
        return False

    return (
        increasing_straight(password)
        and forbidden_chars(password)
        and non_overlapping_doubles(password)
    )


def increment_password(password):
    digits = [ord(digit) for digit in password]
    digits[-1] += 1

    for i in reversed(range(len(digits))):
        if digits[i] == 123:
            digits[i] = 97
            digits[i - 1] += 1

    new_password = ""
    for digit in digits:
        new_password += chr(digit)

    return new_password


def get_valid_password(password):
    is_valid = False
    final_password = password
    attempts = 0

    while not is_valid:
        print(f"{final_password} is not valid -- trying again (Attempt {attempts})")
        final_password = increment_password(final_password)
        is_valid = check_password(final_password)
        attempts += 1

    return final_password


if __name__ == "__main__":
    pt_1 = get_valid_password("cqjxjnds")
    pt_2 = get_valid_password("cqjxxyzz")
    print(f"Solution 1: Next valid password is {pt_1}")
    print(f"Solution 2: Next valid password is {pt_2}")
