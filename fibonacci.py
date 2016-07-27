# first, simple recursion

def fib_simple_recursion( n ):

    # base case
    if n < 2:
        return n

    # regular recursion
    else:
        return fib_simple_recursion(n-1) + fib_simple_recursion(n-2)

print fib_simple_recursion(10)
