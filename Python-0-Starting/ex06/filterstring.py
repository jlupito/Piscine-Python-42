import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3 or not isinstance(sys.argv[1], str):
            raise AssertionError("The arguments are bad.")
        S = sys.argv[1]

        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("The arguments are bad.")
        if N < 0:
            raise AssertionError("The arguments are bad.")

        W = S.split()
        for word in W:
            if not word.isalnum():
                raise AssertionError("The arguments are bad.")

        result = ft_filter(lambda word: len(word) > N, W)

        print(result)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
