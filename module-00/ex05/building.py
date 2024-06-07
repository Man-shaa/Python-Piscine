import sys
import string


def countChar(text) -> None:
    """
    This function counts and prints the number of uppercase letters,\
    lowercase letters,
    punctuation marks, spaces, and digits in the given text.
    """
    count_uppercase = sum(1 for char in text if char.isupper())
    count_lowercase = sum(1 for char in text if char.islower())
    count_punctuation = sum(1 for char in text if char in string.punctuation)
    count_spaces = sum(1 for char in text if char.isspace())
    count_digits = sum(1 for char in text if char.isdigit())
    print("The text contains", len(text), "characters:")
    print(count_uppercase, "upper letters")
    print(count_lowercase, "lower letters")
    print(count_punctuation, "punctuation marks")
    print(count_spaces, "spaces")
    print(count_digits, "digits")


def main():
    if (len(sys.argv) != 2):
        print("ERROR")
        return (1)
    countChar(sys.argv[1])
    return (0)


if __name__ == '__main__':
    main()
