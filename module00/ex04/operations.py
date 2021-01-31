from sys import argv

error_string = '''\
Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3'''

if len(argv) < 3:
    print(error_string)
elif len(argv) > 3:
    print('InputError: too many arguments\n\n' + error_string)
else:
    try:
        int_argv = [int(arg) for arg in argv[1:]]
        print('Sum:         ' + str(int_argv[0] + int_argv[1]))
        print('Difference:  ' + str(int_argv[0] - int_argv[1]))
        print('Product:     ' + str(int_argv[0] * int_argv[1]))
        if int_argv[1] == 0:
            print('Quotient:    ERROR (div by zero)')
            print('Remainder:   ERROR (modulo by zero)')
        else:
            print('Quotient:    ' + str(int_argv[0] / int_argv[1]))
            print('Remainder:   ' + str(int_argv[0] % int_argv[1]))
    except Exception:
        print('InputError: only numbers\n\n' + error_string)
