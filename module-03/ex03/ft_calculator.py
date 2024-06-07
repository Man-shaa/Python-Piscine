class calculator:
    """A simple calculator class that performs basic arithmetic operations on\
    a list of numbers."""
    def __init__(this, object) -> None:
        """Initialize the calculator object with a list of numbers."""
        this.object = object

    def __add__(this, object) -> None:
        """Add a given number to each element in the list."""
        this.object = [x + object for x in this.object]
        print(this.object)

    def __mul__(this, object) -> None:
        """Multiply each element in the list by a given number."""
        this.object = [x * object for x in this.object]
        print(this.object)

    def __sub__(this, object) -> None:
        """Subtract a given number from each element in the list."""
        this.object = [x - object for x in this.object]
        print(this.object)

    def __truediv__(this, object) -> None:
        """Divide each element in the list by a given number."""
        if object == 0:
            print("Division by 0 is not allowed")
            return
        this.object = [x / object for x in this.object]
        print(this.object)


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
