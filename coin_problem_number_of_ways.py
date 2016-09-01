'''
Write a function that given a target amount of money and a list of possible coin denominations, returns the number of ways to make change for the target amount using the coin denominations
'''

def coin_prb( target, coins ):
    # creating our storage
    arr = [1] + [0] * target

    for c in coins:
        for j in range( c, target+1 ):
            print( arr[j], arr[j-c] )
            arr[j] = arr[j] + arr[j-c]

    if target == 0:
        return target
    else:
        print( arr )
        return arr[target]



# test
print( coin_prb( 13, [1,5,10] ) ) 