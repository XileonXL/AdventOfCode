import re


def part_1(lines: list[str]) -> int:
    """
    Process the list of lines to calculate the sum of all valid mul(x, y) operations.

    Args:
        lines (list[str]): The list of lines from the input.

    Returns:
        int: The total sum of the mul(x, y) operations.
    """
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    result = 0

    for line in lines:
        result += sum(
            int(match.group(1)) * int(match.group(2))
            for match in re.finditer(regex, line)
        )

    return result


def part_2(lines: list[str]) -> int:
    """
    Process the list of lines to calculate the sum of all enabled mul(x, y) operations,
    considering 'do()' and 'don't()' instructions that control whether mul is enabled.

    Args:
        lines (list[str]): The list of lines from the input.

    Returns:
        int: The total sum of the enabled mul(x, y) operations.
    """
    regex = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"

    mul_enabled = True
    total_sum = 0

    for line in lines:
        for match in re.finditer(regex, line):
            if match.group(0).startswith("mul"):
                if mul_enabled:
                    a = int(match.group(1))
                    b = int(match.group(2))
                    total_sum += a * b
            elif match.group(0) == "do()":
                mul_enabled = True
            elif match.group(0) == "don't()":
                mul_enabled = False

    return total_sum


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    result_1 = part_1(lines)
    result_2 = part_2(lines)

    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")


if __name__ == "__main__":
    main()
