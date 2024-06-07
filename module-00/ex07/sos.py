import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "$": "...-..- ",
    "@": ".--.-. ",
    "À": ".--.- ",
    "Ä": ".-.- ",
    "Å": ".--.- ",
    "È": ".-..- ",
    "É": "..-.. ",
    "Ö": "---. ",
    "Ü": "..-- ",
    "ß": "...--.. ",
}


def transform(string: str):
    """This function converts a given string into its Morse code\
    representation using a predefined dictionary."""
    morse = ""
    for char in string.upper():
        if char in NESTED_MORSE:
            morse += NESTED_MORSE[char]
    return morse


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("tuto : python sos.py [string]")
        s = sys.argv[1]
        if not (s.replace(' ', '').isalnum()):
            raise AssertionError("the arguments are bad")
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return (1)
    print(transform(sys.argv[1]))
    return 0


if __name__ == "__main__":
    main()
