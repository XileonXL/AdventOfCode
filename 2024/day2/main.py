def is_safe(report: list[int]) -> bool:
    """
    Checks if a report is safe. The report is safe if:
    - The levels are all increasing or all decreasing.
    - The difference between consecutive levels is at least 1 and at most 3.

    Args:
        report (list[int]): List of report levels.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if diff < 1 or diff > 3:
            return False

    is_increasing = True
    is_decreasing = True
    for i in range(1, len(report)):
        if report[i] < report[i - 1]:
            is_increasing = False
        if report[i] > report[i - 1]:
            is_decreasing = False

    return is_increasing or is_decreasing


def is_safe_with_one_removal(report: list[int]) -> bool:
    """
    Checks if a report is safe by removing a single level.

    Args:
        report (list[int]): List of report levels.

    Returns:
        bool: True if the report is safe after removing one level, False otherwise.
    """
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True
    return False


def part_1(reports: list[list[int]]) -> int:
    """
    Count how many reports are safe without any removal.

    Args:
        reports (list[list[int]]): List of reports.

    Returns:
        int: The number of safe reports.
    """
    return sum(1 for report in reports if is_safe(report))


def part_2(reports: list[list[int]]) -> int:
    """
    Count how many reports are safe with one level removal.

    Args:
        reports (list[list[int]]): List of reports.

    Returns:
        int: The number of safe reports with one removal.
    """
    return sum(
        1 for report in reports if is_safe(report) or is_safe_with_one_removal(report)
    )


def main():
    reports = []
    with open("input.txt", "r") as file:
        reports = [list(map(int, line.split())) for line in file]

    result_1 = part_1(reports)
    result_2 = part_2(reports)

    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")


if __name__ == "__main__":
    main()
