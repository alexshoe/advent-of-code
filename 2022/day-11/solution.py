import time
from dataclasses import dataclass

from pprint import pprint


@dataclass
class Monkey:
    items: list[int]
    operation: str
    test: int
    throw_to: tuple[int, int]


def parse_input():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    lines = list(filter(("").__ne__, lines))
    lines = [line.lstrip(" ") for line in lines]

    monkeys = []
    for i in range(int(len(lines) / 6)):
        items = [int(x) for x in lines[i * 6 + 1][16::].split(", ")]
        operation = lines[i * 6 + 2][17::].replace("old", "item")
        test = int(lines[i * 6 + 3][18::])
        true = int(lines[i * 6 + 4][24::])
        false = int(lines[i * 6 + 5][26::])
        throw_to = (false, true)
        inspecinspectionsted = 0
        monkeys.append(Monkey(items, operation, test, throw_to))

    return monkeys


def monkey_business(pt: int, verbose: bool = False) -> int:
    monkeys = parse_input()
    divisor = 1
    for m in monkeys:
        divisor *= m.test

    inspections = [0 for _ in monkeys]
    n = 20 if pt == 1 else 10000
    for _ in range(0, n):
        for i, m in enumerate(monkeys):
            for item in m.items:
                inspections[i] += 1

                new_worry = eval(m.operation)
                if pt == 1:
                    final_worry = new_worry // 3
                else:
                    final_worry = new_worry % divisor
                divisible = (final_worry % m.test) == 0
                target_monkey = m.throw_to[divisible]
                monkeys[target_monkey].items.append(final_worry)

                if verbose:
                    print(f"  Monkey inspects an item with a worry level of {item}.")
                    print(
                        f"     Worry level is increased to {new_worry} ({m.operation})."
                    )
                    if pt == 1:
                        print(
                            f"     Monkey gets bored with item. Worry level is divided by 3 to {final_worry}."
                        )
                    if divisible:
                        print(f"     Current worry level is divisible by {m.test}.")
                    else:
                        print(f"     Current worry level is not divisible by {m.test}.")
                    print(
                        f"     Item with worry level {final_worry} is thrown to monkey {target_monkey}."
                    )
            m.items.clear()

    inspections.sort(reverse=True)

    print("")
    if pt == 1:
        print("Part 1 Recap:")
    else:
        print("Part 2 Recap:")
    for i, inspected in enumerate(inspections):
        print(f"      Monkey {i} inspected items {inspected} times")
    print("")
    print(f"MONKEY BUSINESS LEVEL: {inspections[0]*inspections[1]}")
    print(
        "-----------------------------------------------------------------------------------------"
    )


if __name__ == "__main__":
    start_time = time.time()
    monkey_business(1)
    monkey_business(2)
    print(f"-- Total time elapsed: {time.time() - start_time, 7} seconds --")
