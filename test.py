'''
	TEST FILE
'''
def rec_coin_dynam(target,coins,known_results = None):
    '''
    INPUT: This funciton takes in a target amount and a list of possible coins to use.

    OUTPUT: Minimum number of coins needed to make the target.
    '''

    # initializing our 'cache': all known results from calculations
    if known_results == None:
        known_results = [0] * (target+1) # list with '0' values

    # Default output to target
    min_coins = target

    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1

    # Return a known result if it happens to be greater than 0
    elif known_results[target] > 0:
        return known_results[target]

    else:
        # for every coin value that is < than target
        for i in [c for c in coins if c < target]:

            print 'i: {0}'.format(i)

            # Recursive call, note how we include the known results!
            num_coins = 1 + rec_coin_dynam(target-i,coins,known_results)

            print 'num_coins: {0}; min_coins: {1}'.format(num_coins, min_coins)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins


                # Reset the known result
                known_results[target] = min_coins

            print 'inside known_results: {0}'.format(known_results)

    print 'outside known_results: {0}'.format(known_results)
    return min_coins



target = 6
coins = [1,4]

# print rec_coin_dynam(target,coins,known_results)
print rec_coin_dynam(target,coins)
