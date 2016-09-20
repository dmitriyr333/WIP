import math


''' function '''

def is_prime(n):
    if n == 2:
        return 'Prime'
        
    if n % 2 == 0 or n <= 1:
        return 'Not Prime'

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return 'Not prime'
    return 'Prime'

T = [1000000000,1000000001,1000000002,1000000003,1000000004,1000000005,1000000006,1000000007,1000000008,1000000009]

for n in T:
	print( is_prime( n )
