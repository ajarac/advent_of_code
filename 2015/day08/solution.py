def part1(input_text: str) -> str:
    total_code_len = 0
    total_mem_len = 0

    for line in input_text.strip().split('\n'):
        total_code_len += len(line)
        # Remove surrounding quotes, decode escape sequences
        mem_value = bytes(line[1:-1], 'utf-8').decode('unicode_escape')
        total_mem_len += len(mem_value)

    return total_code_len - total_mem_len

def part2(input_text: str) -> str:
    total_code_len = 0
    total_encoded_len = 0

    for line in input_text.strip().split('\n'):
        total_code_len += len(line)

        # Re-encode: escape backslashes and quotes
        encoded = line.replace('\\', '\\\\').replace('"', '\\"')
        encoded = f'"{encoded}"'  # wrap in quotes
        total_encoded_len += len(encoded)

    return total_encoded_len - total_code_len
