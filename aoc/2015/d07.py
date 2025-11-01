import operator
from typing import Callable, NamedTuple

Arg = tuple[str] | tuple[str, str]


class Operation(NamedTuple):
    args: Arg
    func: Callable[..., int]


def parse(raw: str) -> dict[str, Operation]:
    ops = {
        "AND": operator.and_,
        "OR": operator.or_,
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift,
        "NOT": operator.invert,
    }

    def parse_line(line: str) -> tuple[str, Operation]:
        operation, target = map(str.strip, line.split("->"))
        match operation.split(" "):
            case (lhs, operator, rhs):
                return target, Operation((lhs, rhs), ops[operator])
            case (operator, unary):
                return target, Operation((unary,), ops[operator])
            case (unary,):
                return target, Operation((unary,), no_op)
            case _:
                raise

    return dict(map(parse_line, raw.splitlines()))


def p1(ops: dict[str, Operation]) -> int:
    return find(ops, "a")


def p2(ops: dict[str, Operation]) -> int:
    ops["b"] = Operation(args=(str(find(ops, "a")),), func=no_op)
    return find(ops, "a")


def find(ops: dict[str, Operation], target: str) -> int:
    """
    Traverses dependencies to resolve values recursively.

    Assumptions:
    - No logical cycles (redundant cycles when visiting nodes are allowed)
    """
    values: dict[str, int] = {}

    def resolve(op: Operation) -> int:
        if all(map(str.isnumeric, op.args)):
            return op.func(*map(int, op.args))

        args = []
        for arg in op.args:
            if arg.isnumeric():
                resolved_value = int(arg)
            elif arg in values:
                resolved_value = values[arg]
            else:
                resolved_value = resolve(ops[arg])
                values[arg] = resolved_value

            args.append(resolved_value)

        return op.func(*args)

    return resolve(ops[target])


def no_op(x: int) -> int:
    return x


with open("data/aoc/2015/d07.txt") as f:
    data = f.read()

operations = parse(data)
assert p1(operations) == 3176
assert p2(operations) == 14_710
