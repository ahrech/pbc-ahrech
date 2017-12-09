import argparse

from homework_app.fibonacci import fibonacci
from homework_app.numbers_pairs import numbers_pairs

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This app prints numbers pairs and/or fibonacci numbers.")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--number", "-n", action='store', nargs='+', help="Prints number pairs.", type=int)
    group.add_argument("--fib", "-f", action='store', help="Prints Fibonacci numbers.", type=int)
    args = parser.parse_args()

    if not args.number and not args.fib:
        print "Please specify at least one argument."

    if args.number:
        print "Sum of these pairs of numbers is 10: {}".format(list(numbers_pairs(*args.number)))

    if args.fib:
        print "First {} Fibonacci numbers: {}".format(args.fib, fibonacci(args.fib))
