from sys import argv


def print_even_odd_zero(d):
    if d == 0:
        print("I'm Zero.")
    elif d % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


try:
    if len(argv) == 1:
        pass
    elif len(argv) > 2:
        raise Exception
    else:
        d = int(argv[1])
        print_even_odd_zero(d)
except Exception:
    print('ERROR')
