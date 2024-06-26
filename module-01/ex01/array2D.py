def parse_input(family: list, start: int, end: int) -> int:
    """Validate the input list and indices for slicing."""
    if not isinstance(family, list):
        raise TypeError("Input must be a list")
    if (len(family) == 0):
        raise ValueError("The list is empty")
    if (not all(isinstance(sublist, list) for sublist in family)):
        raise TypeError("Sublists must be lists")
    sublist_lengths = set(len(sublist) for sublist in family)
    if (len(sublist_lengths) != 1):
        raise ValueError("Sublists must be of the same size")
    if (start < 0):
        raise AssertionError("Start index is negative")
    if (start > len(family)):
        raise IndexError("Start index is out of range")
    return (0)


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a given list 'family' from index 'start' to 'end'."""
    if (parse_input(family, start, end) != 0):
        return (None)
    print("My shape is:", (len(family), len(family[0])))
    truncated_list = family[start:end]
    print("My new shape is:", (len(truncated_list), len(truncated_list[0])))
    return (truncated_list)


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return (1)


if __name__ == "__main__":
    main()
