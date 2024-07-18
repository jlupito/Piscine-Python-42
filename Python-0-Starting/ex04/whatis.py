import sys

import sys

def is_integer(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False
if len(sys.argv) == 1:
    print("")
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided\n")
else:
    try:
        int(sys.argv[1])
        number = int(sys.argv[1])
        if number % 2 == 0:
            print("I'm even.\n")
        else:
            print("I'm odd.\n")
    except ValueError:
        print("AssertionError: argument is not an integer\n")