#!/usr/bin/env python3

def print_fibonacci(length):
    """Print a list containing the Fibonacci sequence up to `length` items.

    The function prints the list (using the builtin print) and returns None.
    Examples:
        print_fibonacci(0)  # prints []
        print_fibonacci(1)  # prints [0]
        print_fibonacci(5)  # prints [0, 1, 1, 2, 3]
    """
    if length <= 0:
        print([])
        return

    fib = [0]
    if length == 1:
        print(fib)
        return

    fib.append(1)
    for _ in range(2, length):
        fib.append(fib[-1] + fib[-2])

    print(fib)