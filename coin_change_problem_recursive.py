def rec_coin_dynam(target,coins, known_results = None):
    '''
    INPUT: This funciton takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter shoud be started with [0] * (target+1)

    OUTPUT: Minimum number of coins needed to make the target.
    '''

    if known_results == None:
        known_results = [0] * (target+1)

    # Default output to target
    min_coins = target

    # Base Case
    if target in coins:
        print 'insde Base Case, target: {0}\n'.format(target)
        # known_results[target] = 1
        return 1

    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]

    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:

            print 'i: {0}'.format(i)

            # Recursive call, note how we include the known results!
            num_coins = 1 + rec_coin_dynam(target-i,coins,known_results)

            print 'min_coins: {0}; num_coins: {1}; target: {2}; know_results: {3}'.format(min_coins,num_coins,target,known_results)

            # Reset Minimum if we have a new minimum
            if  min_coins > num_coins:

                print 'inside "if" min_coins: {0}; num_coins: {1}'.format(min_coins,num_coins)
                min_coins = num_coins

                # Reset the known result
                known_results[target] = min_coins

    print known_results
    return min_coins


def main():
  target = 31
  coins = [1,10,25]
  # known_results = [0]*(target+1)

  print rec_coin_dynam(target,coins)
main()
