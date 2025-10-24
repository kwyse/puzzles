import itertools as it


def p1(data: str) -> int:
    forbidden_pairs = {
        "b": "a",
        "d": "c",
        "q": "p",
        "y": "x",
    }

    def is_nice(line: str) -> bool:
        vowels = 0
        last_c: str | None = None
        double_c = False

        for c in line:
            if (prev := forbidden_pairs.get(c)) and prev == last_c:
                return False

            if c == last_c:
                double_c = True

            if c in "aeiou":
                vowels += 1

            last_c = c

        return vowels >= 3 and double_c

    return len([line for line in data.splitlines() if is_nice(line)])


def p2(data: str) -> int:
    """
    Returns the number of strings that are "nice".

    Note `enumerate` starts at index `1`. This is so that we consider repeat pairs
    where the first pair is at the start of the string.

    """

    def is_nice(line: str) -> bool:
        pairs: dict[tuple[str, str], int] = dict()
        prev_c1 = None

        repeat_pair_found = False
        triplet_found = False

        for i, pair in enumerate(it.pairwise(line), start=1):
            if (prev_i := pairs.get(pair)) and i - prev_i >= 2:
                repeat_pair_found = True

            c1, c2 = pair
            if c2 == prev_c1:
                triplet_found = True

            if pair not in pairs:
                pairs[pair] = i

            if repeat_pair_found and triplet_found:
                return True

            prev_c1 = c1

        return False

    return len([line for line in data.splitlines() if is_nice(line)])


with open("data/aoc/2015/d05.txt") as f:
    data = f.read()

assert p1(data) == 258
assert p2(data) == 53
