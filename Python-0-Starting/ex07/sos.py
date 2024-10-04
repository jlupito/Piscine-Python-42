import sys


def main():
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
        if morse[-1].isspace():
            morse = morse[:-1]

        print(morse)

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()
