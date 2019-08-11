class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        MAX = float('inf')

        # 0,inf,inf...
        solution = [0] + [MAX] * amount

        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    solution[i] = min(solution[i-c] + 1, solution[i])

        print(solution)
        if solution[amount] == float('inf'):
            return -1

        return solution[amount]
