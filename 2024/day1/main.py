from collections import Counter


def part_1(col_1: list[int], col_2: list[int]) -> int:
    """
    Calculates the sum of the absolute differences between corresponding
    elements of two lists after sorting them.

    Args:
        col_1 (list[int]): The first list of integers.
        col_2 (list[int]): The second list of integers.

    Returns:
        int: The sum of the absolute differences between the corresponding
             elements of the lists.
    """

    return sum(abs(a - b) for a, b in zip(sorted(col_1), sorted(col_2)))


def part_2(col_1: list[int], col_2: list[int]) -> int:
    """
    Calculates the sum of the products of the elements in col_1 with the number of
    occurrences of those elements in col_2.

    Args:
        col_1 (list[int]): The first list of integers.
        col_2 (list[int]): The second list of integers.

    Returns:
        int: The sum of the products between the elements of col_1 and their
             occurrences in col_2.
    """

    # Use Counter to count the occurrences of elements in col_2
    occurrences = Counter(col_2)
    return sum(number * occurrences.get(number, 0) for number in col_1)


def main():
    col_1 = []
    col_2 = []
    with open("input.txt", "r") as file:
        for line in file:
            a, b = map(int, line.split())
            col_1.append(a)
            col_2.append(b)

    result_1 = part_1(col_1, col_2)
    result_2 = part_2(col_1, col_2)

    print(f"Result 1: {result_1}")
    print(f"Result 1: {result_2}")


if __name__ == "__main__":
    main()
