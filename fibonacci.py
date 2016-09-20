# 0,1,1,2,3,5,8,13...

# first, simple recursion
def fib_simple_recursion( n ):

    # base case
    if n < 2:
        return n

    # regular recursion
    else:
        return fib_simple_recursion(n-1) + fib_simple_recursion(n-2)


# Dynamic programming:

def fib_dynamic(n):

    memo = dict()

    if n < 2:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib_dynamic(n-1) + fib_dynamic(n-2)
            return memo[n]



# Iterate over
def fib_iterate(n):
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a+b

    return a


''' test '''
print( fib_simple_recursion(10)
print( fib_dynamic(10)
print( fib_iterate(10)
