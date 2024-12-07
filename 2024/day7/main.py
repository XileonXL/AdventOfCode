from itertools import product


def evaluate_expression(nums: list[int], operator_combinations: tuple[str, ...]) -> int:
    """
    Evaluates an expression represented by a list of numbers and operator_combinations, left-to-right.

    Args:
        nums (list[int]): List of numbers.
        operator_combinations (list[str]): List of operators ('+', '*', or '||').

    Returns:
        int: The result of evaluating the expression.
    """
    result = nums[0]
    for i, op in enumerate(operator_combinations):
        if op == "+":
            result += nums[i + 1]
        elif op == "*":
            result *= nums[i + 1]
        elif op == "||":
            result = int(str(result) + str(nums[i + 1]))
    return result


def is_solvable(test_value: int, nums: list[int], operators: list[str]) -> bool:
    """
    Determines if a test value can be produced by combining the numbers with the given operators.

    Args:
        test_value (int): The target value to match.
        nums (list[int]): List of numbers to use in the equation.
        operators (list[str]): List of allowed operators ('+', '*', or '||').

    Returns:
        bool: True if the test value can be produced, False otherwise.
    """
    num_positions = len(nums) - 1
    for operator_combinations in product(operators, repeat=num_positions):
        if evaluate_expression(nums, operator_combinations) == test_value:
            return True
    return False


def get_total_calibration_result(lines: list[str], operators: list[str]) -> int:
    """
    Calculates the total calibration result by summing test values that can be solved with the given operators.

    Args:
        lines (list[str]): List of input lines, where each line is in the format "test_value: nums".
        operators (list[str]): List of allowed operators ('+', '*', or '||').

    Returns:
        int: The total calibration result.
    """
    result = 0
    for line in lines:
        parts = line.split(":")
        test_value = int(parts[0].strip())
        nums = list(map(int, parts[1].strip().split()))
        if is_solvable(test_value, nums, operators):
            result += test_value
    return result


def part_1(lines: list[str]) -> int:
    """
    Calculates the total calibration result by summing test values that can be solved using '+' and '*'.

    Args:
        lines (list[str]): List of input lines, where each line is in the format "test_value: nums".

    Returns:
        int: The total calibration result.
    """
    return get_total_calibration_result(lines, ["+", "*"])


def part_2(lines: list[str]) -> int:
    """
    Calculates the total calibration result by summing test values that can be solved using '+', '*', and '||'.

    Args:
        lines (list[str]): List of input lines, where each line is in the format "test_value: nums".

    Returns:
        int: The total calibration result.
    """
    return get_total_calibration_result(lines, ["+", "*", "||"])


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    result_1 = part_1(lines)
    result_2 = part_2(lines)
    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")


if __name__ == "__main__":
    main()
