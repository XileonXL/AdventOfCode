def parse_rules(rules: list[str]) -> dict[int, set[int]]:
    """Parse the list of rules of type XX|XX

    Args:
        rules (list[str]): The list of lines from the input.

    Returns:
        dict[int, set[int]]: A dictionary where each key is an integer, and its value
                             is a set of integers that must come after the key in the
                             order defined by the rules.
    """
    parsed_rules = {}
    for rule in rules:
        val_1, val_2 = map(int, rule.split("|"))
        if val_1 not in parsed_rules:
            parsed_rules[val_1] = {val_2}
        else:
            parsed_rules[val_1].add(val_2)

    return parsed_rules


def part_1(rules: list[str], updates: list[str]) -> int:
    """
    Processes the list of page update sequences to determine if each update
    follows the specified page ordering rules. If the update follows the rules,
    the middle page number is added to the result.

    Args:
        rules (list[str]): A list of strings, where each string represents a
                           page ordering rule in the format 'X|Y', indicating
                           that page X must come before page Y.
        updates (list[str]): A list of comma-separated strings, each representing
                             a sequence of page numbers that need to be checked
                             against the ordering rules.

    Returns:
        int: The sum of the middle page number from each valid update, where an
             update is considered valid if it follows the page ordering rules.

    """
    parsed_rules = parse_rules(rules)

    result = 0
    for update in updates:
        is_valid = True
        values = list(map(int, update.split(",")))
        for val in values:
            for i in range(values.index(val)):
                if values[i] in parsed_rules[val]:
                    is_valid = False

        if is_valid:
            result += values[len(values) // 2]

    return result


def part_2(rules: list[str], updates: list[str]) -> int:
    """
    Processes the list of page update sequences to identify invalid updates based on
    the specified page ordering rules. For each invalid update, the page numbers
    are reordered according to the rules, and the middle page number is added to the result.

    Args:
        rules (list[str]): A list of strings, where each string represents a
                           page ordering rule in the format 'X|Y', indicating
                           that page X must come before page Y.
        updates (list[str]): A list of comma-separated strings, each representing
                             a sequence of page numbers that need to be checked
                             against the ordering rules.

    Returns:
        int: The sum of the middle page number from each invalid update, where an
             update is considered invalid if it does not follow the page ordering rules.
             The page numbers of invalid updates are reordered according to the rules
             before determining the middle page number.
    """

    parsed_rules = parse_rules(rules)

    incorrect_updates = []
    for update in updates:
        is_valid = True
        values = list(map(int, update.split(",")))
        for val in values:
            for i in range(values.index(val)):
                if values[i] in parsed_rules[val]:
                    is_valid = False
        if not is_valid:
            incorrect_updates.append(values)

    result = 0
    for incorrect_update in incorrect_updates:
        for i in range(len(incorrect_update)):
            for j in range(i, len(incorrect_update)):
                if incorrect_update[i] == incorrect_update[j]:
                    continue
                if incorrect_update[i] in parsed_rules[incorrect_update[j]]:
                    (
                        incorrect_update[j],
                        incorrect_update[i],
                    ) = (
                        incorrect_update[i],
                        incorrect_update[j],
                    )
        result += incorrect_update[len(incorrect_update) // 2]

    return result


def main():
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]

    separator_index = lines.index("")

    rules = lines[:separator_index]
    updates = lines[separator_index + 1 :]

    result_1 = part_1(rules, updates)
    result_2 = part_2(rules, updates)

    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")

    return 0


if __name__ == "__main__":
    main()
