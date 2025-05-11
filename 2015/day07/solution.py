from typing import Dict, Optional, Union


class Operation:
    def __init__(self, op: Optional[str], left: Optional[str], right: Optional[str]):
        self.op = op
        self.left = left
        self.right = right


def parse(input_text: str) -> Dict[str, Operation]:
    operations = {}
    for row in input_text.strip().split('\n'):
        expr, wire = row.split("->")
        wire = wire.strip()
        tokens = expr.strip().split()

        if len(tokens) == 1:
            # direct assignment: e.g., 123 -> x
            operations[wire] = Operation(None, tokens[0], None)
        elif len(tokens) == 2:
            # unary NOT: e.g., NOT x -> h
            operations[wire] = Operation(tokens[0], tokens[1], None)
        elif len(tokens) == 3:
            # binary op: e.g., x AND y -> z
            operations[wire] = Operation(tokens[1], tokens[0], tokens[2])
    return operations


def evaluate(wire: str, ops: Dict[str, Operation], cache: Dict[str, int]) -> int:
    if wire.isdigit():
        return int(wire)

    if wire in cache:
        return cache[wire]

    op = ops[wire]

    def val(operand: Optional[str]) -> int:
        return evaluate(operand, ops, cache) if operand and not operand.isdigit() else int(operand)

    if op.op is None:
        result = val(op.left)
    elif op.op == "NOT":
        result = ~val(op.left)
    elif op.op == "AND":
        result = val(op.left) & val(op.right)
    elif op.op == "OR":
        result = val(op.left) | val(op.right)
    elif op.op == "LSHIFT":
        result = val(op.left) << val(op.right)
    elif op.op == "RSHIFT":
        result = val(op.left) >> val(op.right)
    else:
        raise ValueError(f"Unknown operation: {op.op}")

    result &= 0xFFFF  # mask to 16-bit
    cache[wire] = result
    return result


def part1(input_text: str) -> str:
    operations = parse(input_text)
    cache = {}
    result = evaluate('a', operations, cache)
    return f"Signal on wire a: {result}"


def part2(input_text: str) -> str:
    operations = parse(input_text)
    cache = {}
    a_value = evaluate('a', operations, cache)

    # Override 'b' with result from part1 and re-evaluate
    operations = parse(input_text)
    operations['b'] = Operation(None, str(a_value), None)
    cache = {}
    result = evaluate('a', operations, cache)
    return f"New signal on wire a (after overriding b): {result}"
