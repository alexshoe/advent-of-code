def calculate_paper(l, w, h):
    surface_area = (2 * l * w) + (2 * w * h) + (2 * h * l)
    slack = min(l * w, w * h, l * h)
    return surface_area + slack


def calculate_ribbon(l, w, h):
    side_1, side_2 = sorted([l, w, h])[0:2]

    ribbon_wrap = (2 * side_1) + (2 * side_2)
    ribbon_top = l * w * h
    return ribbon_wrap + ribbon_top


def total_materials_needed():
    with open("input.txt") as f:
        boxes = f.read().splitlines()

    total_paper = 0
    total_ribbon = 0
    for box in boxes:
        l, w, h = [int(dimension) for dimension in box.split("x")]
        total_paper += calculate_paper(l, w, h)
        total_ribbon += calculate_ribbon(l, w, h)

    return total_paper, total_ribbon


if __name__ == "__main__":
    total_paper, total_ribbon = total_materials_needed()
    print(f"Solution 1: {total_paper} sq feet of wrapping paper")
    print(f"Solution 2: {total_ribbon} feet of ribbon")
