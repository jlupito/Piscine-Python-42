import sys

try:
    if len(sys.argv) == 1:
        print("")
    elif len(sys.argv) > 2:
        raise AssertionError("The arguments are bad.")
    else:
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("The arguments are bad.")
        if number % 2 == 0:
            print("I'm even.\n")
        else:
            print("I'm odd.\n")

except AssertionError as e:
    print(e)