def NULL_not_found(object: any) -> int:
    match object:
        case None:
            return (print("Nothing : None", type(object)), 0)
        case float():
            return (print("Cheese : nan", type(object)), 0)
        case 0 if not isinstance(object, bool) and isinstance(object, int):
            return (print("Zero : 0", type(object)), 0)
        case '':
            return (print("Empty:", type(object)), 0)
        case False:
            return (print("Fake: False", type(object)), 0)
    return (1)


# def main():
#     Nothing = None
#     Garlic = float("NaN")
#     Zero = 0
#     Empty = ''
#     Fake = False
#     NULL_not_found(Nothing)
#     NULL_not_found(Garlic)
#     NULL_not_found(Zero)
#     NULL_not_found(Empty)
#     NULL_not_found(Fake)
#     print(NULL_not_found("Brian"))


# if __name__ == "__main__":
#     main()
