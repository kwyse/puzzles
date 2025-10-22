import hashlib as ha


def p1(data: str) -> int:
    return find_prefix(data, 5)


def p2(data: str) -> int:
    return find_prefix(data, 6)


def find_prefix(data: str, size: int) -> int:
    n = 0
    while True:
        hash = ha.md5(f"{data.strip()}{n}".encode()).hexdigest()
        if hash.startswith("0" * size):
            return n

        n += 1


with open("data/aoc/2015/d04.txt") as f:
    data = f.read()


assert p1(data) == 254_575
assert p2(data) == 1_038_736
