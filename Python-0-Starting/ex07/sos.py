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
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- "}


def main():

    try:
        s = sys.argv[1]
        if len(sys.argv) != 2 or not isinstance(s, str):
            raise AssertionError("The arguments are bad")
        for char in s:
            if not char.isspace() and not char.isalnum():
                raise AssertionError("The arguments are bad")

        morse = ""
        for char in s:
            morse += NESTED_MORSE[char.upper()]
        print(morse)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
