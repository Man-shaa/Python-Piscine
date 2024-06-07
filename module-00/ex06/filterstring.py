import sys


def parse_arg(args):
    """This function validates the command-line arguments, ensuring there\
    are exactly three,
    the first argument is an alphanumeric string, and the second is a digit."""
    if (len(args) != 3):
        raise AssertionError("tuto : \"python filterstring \
            [string] [number]\"")
    if (not args[1].replace(' ', '').isalnum()):
        raise AssertionError("first argument must be a string")
    if (not args[2].isdigit()):
        raise AssertionError("second argument must be a number")
    return (0)


def filter_string(string, condition):
    """This function filters a given string, returning a list of words\
    that satisfy the specified condition."""
    return [word for word in string.split() if condition(word)]


def main():
    if (parse_arg(sys.argv) == 1):
        return (1)
    print(filter_string(str(sys.argv[1]), lambda x: len(x) > int(sys.argv[2])))
    return (0)


if __name__ == "__main__":
    main()
