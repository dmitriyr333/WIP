from math import sqrt
import numpy as np

def compute_median( arr ):
    mid = len( arr ) // 2
    
    # even
    if len( arr ) % 2 == 0:
        # print( (arr[mid-1], arr[mid])
        return float(arr[mid-1] + arr[mid]) / 2
    # odd
    else:
        return float(arr[mid])


def compute_mean( arr ):
    return sum(arr) / len(arr)

def standard_deviation( arr ):
    median = compute_median( arr )
    mean = compute_mean( arr )
    # print('arr: {}, median computed: {}, median numpy: {}'.format(arr, median, np.median(arr)))

    sum_val = 0

    for elem in arr:
        calc = ( elem - mean ) ** 2
        sum_val += calc
        #30466.9
    
    # print(  sum_val / len(arr) )
        
    
    print( '{0:0.1f}'.format( sqrt( sum_val / len(arr) ) ) )

def solution( n, X, F ):
    data = []

    for i in range( n ):
        # data.append( X[i] * F[i] )
        for j in range( F[i] ):
            data.append( X[i] )
    
    data.sort()

    # finding full mid
    mid = len(data) // 2

    # even
    if len(data) % 2 == 0:
        mid_low  = mid // 2
        mid_high = mid + mid_low
    # odd
    else: 
        mid_low  = mid // 2
        # mid_high = mid + mid_low
        mid_high = mid + (len(data[:mid+1]) // 2)
    
    # quartile caclulations
    if len(data[:mid]) % 2 == 0:
        print( 'even half' )
        q1 = (data[mid_low-1] + data[mid_low] ) / 2 
        q3 = (data[mid_high-1] + data[mid_high] ) / 2 
    else:
        print( 'odd half' )
        q1 = data[mid_low-1] 
        q3 = data[mid_high] 



    print( 'data: {}; len: {}; mid: {}; median: {}'.format(data, len(data), mid, compute_median(data) ) )
    print( 'mid_low: {}; mid_high: {}'.format(data[mid_low], data[mid_high]) )
    print( '{0:0.1f}'.format(q3-q1) )

# test
n = int('10')
arr = [int(x) for x in '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'.split() ]
standard_deviation(sorted(arr))



# n = int('6')
# X = [int(x) for x in '6 12 8 10 20 16'.split()]
# F = [int(x) for x in '5 4 3 2 1 5'.split()]


# n = int('6')
# X = [int(x) for x in '6 12 8 10 20 16'.split()]
# F = [int(x) for x in '5 6 7 8 9 10'.split()]


# n = int('5')
# X = [int(x) for x in '10 40 30 50 20'.split()]
# F = [int(x) for x in '1 2 3 4 5'.split()]

# solution( n, X, F)