import sys


def ft_check_character(text: str) -> None:
    """
    Takes a single string argument and displays the sums of
    its upper-case characters, lower-case characters,
    punctuation characters, digits and spaces.

    Args:
        text (str): the text to analyse.

    Returns:
        None: the function prints the results of the analysis.
    """
    up_char = 0
    low_char = 0
    digit = 0
    space = 0
    punct_char = 0
    punct_set = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

    for char in text:
        if char.isupper():
            up_char += 1
        elif char.islower():
            low_char += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        elif char in punct_set:
            punct_char += 1

    total_char = up_char + low_char + digit + space + punct_char

    print(f"The text contains {total_char} characters:")
    print(f"{up_char} upper letters")
    print(f"{low_char} lower letters")
    print(f"{punct_char} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():

    try:
        if len(sys.argv) > 2:
            raise AssertionError("The arguments are bad")

        elif len(sys.argv) == 1:
            user_input = ""
            while user_input == "":
                user_input = input("Please enter a string: ")
            if not isinstance(user_input, str):
                raise AssertionError("The arguments are bad")
            ft_check_character(user_input)

        else:
            if not isinstance(sys.argv[1], str):
                raise AssertionError("The arguments are bad")
            ft_check_character(sys.argv[1])

        return

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
