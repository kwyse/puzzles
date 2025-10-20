import itertools as it
import math as ma


Dims = tuple[int, int, int]


def parse(raw: str) -> list[Dims]:
    def parse_line(line: str) -> Dims:
        return Dims(int(c) for c in line.split("x"))

    return [parse_line(line) for line in raw.splitlines()]


def p1(all_dims: list[Dims]) -> int:
    def calc(dims: Dims) -> int:
        smallest_side = ma.prod(sorted(dims)[0:2])
        sides = it.combinations(dims, 2)
        return sum(2 * ma.prod(s) for s in sides) + smallest_side

    return sum(calc(dims) for dims in all_dims)


def p2(all_dims: list[Dims]) -> int:
    def calc(dims: Dims) -> int:
        perimeter = sum(s * 2 for s in sorted(dims)[0:2])
        volume = ma.prod(dims)
        return perimeter + volume

    return sum(calc(dims) for dims in all_dims)


with open("data/aoc/2015/d02.txt") as f:
    data = f.read()

all_dims = parse(data)
assert p1(all_dims) == 1_588_178
assert p2(all_dims) == 3_783_758
