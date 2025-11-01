def p1(data: str) -> int:
    size = 1000
    lights = [0] * size
    for line in data.splitlines():
        com1, *com2, coord1, _, coord2 = line.split(" ")
        x1, y1 = map(int, coord1.split(","))
        x2, y2 = map(int, coord2.split(","))

        x2 += 1
        for y in range(y1, y2 + 1):
            match com1, com2:
                case "turn", ["on"]:
                    lights[y] = set_bits(lights[y], x1, x2)
                case "turn", ["off"]:
                    lights[y] = unset_bits(lights[y], x1, x2)
                case "toggle", []:
                    lights[y] = toggle_bits(lights[y], x1, x2)
                case _:
                    raise

    return sum(map(int.bit_count, lights))


def p2(data: str) -> int:
    size = 1000
    lights = [[0 for _ in range(size)] for _ in range(size)]
    for line in data.splitlines():
        com1, *com2, coord1, _, coord2 = line.split(" ")
        x1, y1 = map(int, coord1.split(","))
        x2, y2 = map(int, coord2.split(","))

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                match com1, com2:
                    case "turn", ["on"]:
                        lights[y][x] += 1
                    case "turn", ["off"]:
                        lights[y][x] = max(lights[y][x] - 1, 0)
                    case "toggle", []:
                        lights[y][x] += 2
                    case _:
                        raise

    return sum(light for row in lights for light in row)


def set_bits(n: int, start: int, end: int) -> int:
    "Set `[start, end)` bits."

    msb = 1 << end - start
    mask = msb - 1 << start
    return n | mask


def unset_bits(n: int, start: int, end: int) -> int:
    "Unset `[start, end)` bits."

    msb_len = max(n.bit_length(), end)
    msb = 1 << msb_len - end
    msb_mask = msb - 1 << end
    lsb_mask = (1 << start) - 1
    mask = msb_mask | lsb_mask
    return n & mask


def toggle_bits(n: int, start: int, end: int) -> int:
    "Flip `[start, end)` bits."

    msb_len = max(n.bit_length(), end)
    msb = (1 << msb_len - end) - 1 << end
    lsb = (1 << start) - 1

    isolated = ((1 << end - start) - 1) << start
    flipped = ~(n & isolated) & isolated

    return (n & msb) | flipped | (n & lsb)


with open("data/aoc/2015/d06.txt") as f:
    data = f.read()

assert p1(data) == 569_999
assert p2(data) == 17_836_115
