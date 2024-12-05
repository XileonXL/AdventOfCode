def part_1(lines: list[str]) -> int:
    """
    Count all occurrences of the word XMAS in the grid, considering all directions.

    Args:
        lines (list[str]): A list of string lines

    Returns:
        int: Total count of the word found in the grid.
    """
    word = "XMAS"
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Horizontal right
        (1, 0),  # Vertical down
        (1, 1),  # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (0, -1),  # Horizontal left
        (-1, 0),  # Vertical up
        (-1, -1),  # Diagonal up-left
        (-1, 1),  # Diagonal up-right
    ]
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_word(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_word(x, y, dx, dy):
                    count += 1

    return count


def part_2(lines: list[str]) -> int:
    """
    Count all occurrences of "X-MAS" patterns in the grid.

    Args:
        lines (list[str]): A list of string lines

    Returns:
        int: Total count of "X-MAS" patterns found in the grid.
    """
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])
    count = 0

    def is_x_mas(x, y):
        """
        Check if there is an X-MAS pattern centered at grid[x][y].
        """
        # Validate indices for diagonals
        if x - 1 >= 0 and x + 1 < rows and y - 1 >= 0 and y + 1 < cols:
            # Check diagonals for standard orientation
            standard_forward = (
                grid[x - 1][y - 1] == "M"
                and grid[x][y] == "A"
                and grid[x + 1][y + 1] == "S"
            )

            standard_backward = (
                grid[x - 1][y + 1] == "M"
                and grid[x][y] == "A"
                and grid[x + 1][y - 1] == "S"
            )
            # Check diagonals for inverted orientation
            inverted_forward = (
                grid[x + 1][y - 1] == "M"
                and grid[x][y] == "A"
                and grid[x - 1][y + 1] == "S"
            )

            inverted_backward = (
                grid[x + 1][y + 1] == "M"
                and grid[x][y] == "A"
                and grid[x - 1][y - 1] == "S"
            )

        if (standard_forward or inverted_backward) and (
            standard_backward or inverted_forward
        ):
            return True
        return False

    # Iterate over the grid to find X-MAS patterns
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if is_x_mas(x, y):
                count += 1

    return count


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    result_1 = part_1(lines)
    result_2 = part_2(lines)

    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")

    return 0


if __name__ == "__main__":
    main()
