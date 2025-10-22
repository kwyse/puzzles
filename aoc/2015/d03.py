import itertools as it

Coord = tuple[int, int]

moves = {
    "^": lambda x, y: (x, y + 1),
    "v": lambda x, y: (x, y - 1),
    ">": lambda x, y: (x + 1, y),
    "<": lambda x, y: (x - 1, y),
}


def p1(data: str) -> int:
    pos = (0, 0)
    visited: set[Coord] = set([pos])
    for c in data.strip():
        pos = moves[c](*pos)
        visited.add(pos)

    return len(visited)


def p2(data: str) -> int:
    santa: Coord = (0, 0)
    robo: Coord = (0, 0)
    visited: set[Coord] = set([santa])
    for s, r in it.batched(data.strip(), 2):
        santa = moves[s](*santa)
        robo = moves[r](*robo)
        visited.add(santa)
        visited.add(robo)

    return len(visited)


with open("data/aoc/2015/d03.txt") as f:
    data = f.read()

assert p1(data) == 2592
assert p2(data) == 2360
