import sys

def main():
    if len(sys.argv) != 3 or not isinstance(sys.argv[1], str):
        print("AssertionError: the arguments are bad")
        return
    try:
        int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return
    s = sys.argv[1]
    n = int(sys.argv[2])
    is_special_char = lambda char: not char.isalpha() and not char.isspace()
    for char in s:
        if is_special_char(char):
            print("AssertionError: the arguments are bad")
            return

    words_longer_than_n = [word for word in s.split() if len(word) > n]
    print(words_longer_than_n)

if __name__ == "__main__":
    main()