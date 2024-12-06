import copy

DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}
ROTATE_RIGHT = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}
INIT_SYMBOL = "^"


def find_start(grid: list[list[str]], symbol: str = "^") -> tuple[int, int] | None:
    """
    Finds the starting position of a specific symbol in the grid.

    Args:
        grid (list[list[str]]): The 2D grid representing the map.
        symbol (str): The symbol to find in the grid.

    Returns:
        tuple[int, int] | None: The (row, column) position of the symbol, or None if not found.
    """
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == symbol:
                return (i, j)
    return None


def is_out_of_bounds(pos: tuple[int, int], grid: list[list[str]]) -> bool:
    """
    Checks if a position is outside the bounds of the grid.

    Args:
        pos (tuple[int, int]): The position to check (row, column).
        grid (list[list[str]]): The 2D grid.

    Returns:
        bool: True if the position is out of bounds, False otherwise.
    """
    x, y = pos
    return x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])


def simulate_movement(
    grid: list[list[str]], start_pos: tuple[int, int], start_dir: str
) -> bool:
    """
    Simulates the movement of the guard from a starting position and direction,
    and detects if it gets stuck in a loop.

    Args:
        grid (list[list[str]]): The 2D grid representing the map.
        start_pos (tuple[int, int]): The starting position of the guard (row, column).
        start_dir (str): The starting direction of the guard ("^", ">", "v", or "<").

    Returns:
        bool: True if the guard enters a loop, False if it exits the map.
    """
    curr_pos = start_pos
    curr_dir = start_dir
    visited_states = set()

    while True:
        state = (curr_pos, curr_dir)
        if state in visited_states:
            return True
        visited_states.add(state)

        dx, dy = DIRECTIONS[curr_dir]
        next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)

        if is_out_of_bounds(next_pos, grid):
            return False

        if grid[next_pos[0]][next_pos[1]] == "#":
            curr_dir = ROTATE_RIGHT[curr_dir]
        else:
            curr_pos = next_pos


def part_1(lines: list[list[str]]) -> int:
    """
    Calculates the number of distinct positions visited by the guard
    before leaving the map.

    Args:
        lines (list[list[str]]): The 2D grid representing the map.

    Returns:
        int: The number of positions visited.
    """
    grid = copy.deepcopy(lines)
    curr_pos = find_start(grid, INIT_SYMBOL)
    if not curr_pos:
        return 0

    visited = set()
    visited.add(curr_pos)

    dir = INIT_SYMBOL

    while True:
        dx, dy = DIRECTIONS[dir]
        next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)

        if is_out_of_bounds(next_pos, grid):
            break

        if grid[next_pos[0]][next_pos[1]] == "#":
            dir = ROTATE_RIGHT[dir]
        else:
            curr_pos = next_pos
            visited.add(curr_pos)

    return len(visited)


def part_2(lines: list[list[str]]) -> int:
    """
    Determines how many positions can be obstructed to make the guard
    get stuck in a loop.

    Args:
        lines (list[list[str]]): The 2D grid representing the map.

    Returns:
        int: The number of positions where a new obstruction causes a loop.
    """
    grid = copy.deepcopy(lines)

    start_pos = find_start(grid, INIT_SYMBOL)
    if not start_pos:
        return 0

    start_dir = INIT_SYMBOL
    valid_positions = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "." and (i, j) != start_pos:
                grid[i][j] = "#"
                if simulate_movement(grid, start_pos, start_dir):
                    valid_positions += 1
                grid[i][j] = "."

    return valid_positions


def main() -> None:
    with open("input.txt", "r") as file:
        lines = [list(line.strip()) for line in file]

    result_1 = part_1(lines)
    result_2 = part_2(lines)

    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")


if __name__ == "__main__":
    main()
