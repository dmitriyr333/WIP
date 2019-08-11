
def coinz(coins, target):
    # print('here too')

    MAX = float('inf')
    dp = [0] + [MAX]*target

    for i in range(1, target+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i-coin]+1, dp[i])
    if dp[-1] == float('inf'):
        return -1

    return dp[target]


def main():
    # print('{0}'.format("here"))

    coins = [1, 3, 5]
    target = 11
    print('answer: {0}'.format(coinz(coins, target)))


main()
