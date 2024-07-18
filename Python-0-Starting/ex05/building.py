import sys


def ft_check_character(input):
    up_char = 0
    low_char = 0
    digit = 0
    space = 0
    punct = 0
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    for char in input:
        if char.isupper():
            up_char += 1
        elif char.islower():
            low_char += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        elif char in punctuation:
            punct += 1
    total = up_char + low_char + digit + space + punct
    print(f"The text contains {total} characters:")
    print(f"{up_char} upper letters")
    print(f"{low_char} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")

def main():

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    elif len(sys.argv) == 1:
        user_input = ""
        while user_input == "":
            user_input = input("Please enter a string: ")
        ft_check_character(user_input)
    else:
        ft_check_character(sys.argv[1])
    return

if __name__ == "__main__":
    main()