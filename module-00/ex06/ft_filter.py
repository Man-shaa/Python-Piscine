def is_even(n):
    """Check if a number is even."""
    return (n % 2 == 0)


def ft_filter(func, iterable):
    """Filter elements from an iterable based on the given function."""
    return [x for x in iterable if func(x)]


def main():
    numbers = [0, 1, 2, 3, 4, 5, 6]
    filtered_numbers = ft_filter(is_even, numbers)
    print(filtered_numbers)
    return (0)


if __name__ == "__main__":
    main()
