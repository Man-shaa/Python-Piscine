class calculator:
    @classmethod
    def dotproduct(this, V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""
        object = sum(x * y for x, y in zip(V1, V2))
        print(object)

    @classmethod
    def add_vec(this, V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise."""
        object = [float(x + y) for x, y in zip(V1, V2)]
        print(object)

    @classmethod
    def sous_vec(this, V1: list[float], V2: list[float]) -> None:
        """Subtract vector2 from vector1 element-wise."""
        object = [float(x - y) for x, y in zip(V1, V2)]
        print(object)


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)
    return (0)


if __name__ == "__main__":
    main()
