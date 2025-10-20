def parse(raw: str) -> list[int]:
    directions = {
        "(": 1,
        ")": -1,
    }

    return [directions[c] for c in raw.strip()]


def p1(directions: list[int]) -> int:
    return sum(directions)


def p2(directions: list[int]) -> int:
    floor = 0
    for i, d in enumerate(directions, 1):
        floor += d
        if floor < 0:
            return i

    return -1


with open("data/aoc/2015/d01.txt") as f:
    data = f.read()

directions = parse(data)
assert p1(directions) == 74
assert p2(directions) == 1795
