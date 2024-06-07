def all_thing_is_obj(object: any) -> int:
    match object:
        case list():
            print("List :",  type(object))
        case tuple():
            print("Tuple :", type(object))
        case set():
            print("Set :", type(object))
        case dict():
            print("Dict :", type(object))
        case str():
            print(object, "is in the kitchen :", type(object))
        case int():
            print("Type not found")

    return (42)


def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}
    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    all_thing_is_obj("Toto")
    print(all_thing_is_obj(10))


if __name__ == "__main__":
    main()
