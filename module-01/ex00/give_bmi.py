def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the Body Mass Index (BMI) for each pair of height and\
    weight provided in the lists."""
    if len(height) != len(weight):
        raise ValueError("ValueError: Height and weight lists must be of\
        the same length")
    result = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError("ValueError: Height and weight must be integers\
            or floats")
        if h <= 0 or w <= 0:
            raise ValueError("ValueError: Height and weight must be\
            positive values")
        bmi = w/(h**2)
        result.append(bmi)
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Determine whether the BMI values exceed the given limit."""
    return [b > limit for b in bmi]


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    try:
        bmi = give_bmi(height, weight)
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return (1)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
